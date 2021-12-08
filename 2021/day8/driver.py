from pprint import pprint

import click


digits = {
    1: ['c', 'f'],
    2: ['a', 'c', 'd', 'e', 'g'],
    3: ['a', 'c', 'd', 'f', 'g'],
    4: ['b', 'c', 'd', 'f'],
    5: ['a', 'b', 'd', 'f', 'g'],
    6: ['a', 'b', 'd', 'e', 'f', 'g'],
    7: ['a', 'c', 'f'],
    8: ['a', 'b', 'c', 'd', 'e', 'f', 'g'],
    9: ['a', 'b', 'c', 'd', 'f', 'g'],
    0: ['a', 'b', 'c', 'e', 'f', 'g'],
}

num_lines = {}

for digit in digits:
    num_line = len(digits[digit])
    if num_line in num_lines:
        num_lines[num_line].append(digit)
    else:
        num_lines[num_line] = [digit]


def count_segments(inputs, uniq_line_nums):

    count = 0
    for input in inputs:
        for segment in input.split(' '):
            if len(segment) in uniq_line_nums:
                count +=1
    
    return count


def determine_mapping(input):

    mapping = {
        'a': '',
        'b': '',
        'c': '',
        'd': '',
        'e': '',
        'f': '',
        'g': '',
    }

    number_mapping = {
        0: None,
        1: None,
        2: None,
        3: None,
        4: None,
        5: None,
        6: None,
        7: None,
        8: None,
        9: None,
    }

    signals_by_length = {}

    for signal in input["signals"]:
        signal_len = len(signal)
        if signal_len in signals_by_length:
            signals_by_length[signal_len].append(signal)
        else:
            signals_by_length[signal_len] = [signal]
        match signal_len:
            case 2: 
                number_mapping[1] = signal
            case 4: 
                number_mapping[4] = signal
            case 3: 
                number_mapping[7] = signal
            case 7: 
                number_mapping[8] = signal

    mapping['a'] = number_mapping[7] - number_mapping[1]

    for signal in signals_by_length[5]:
        work_diff = signal - number_mapping[7]
        if len(work_diff) == 2:
            number_mapping[3] = signal
            signals_by_length[5].remove(signal)

    for signal in signals_by_length[6]:
        work_diff = signal - number_mapping[3]
        if len(work_diff) == 1:
            number_mapping[9] = signal
            signals_by_length[6].remove(signal)
        
    for signal in signals_by_length[6]:
        signal_union = signal | number_mapping[1]
        if len(signal_union) == 6:
            number_mapping[0] = signal
        else:
            number_mapping[6] = signal
    
    for signal in signals_by_length[5]:
        signal_union = signal | number_mapping[9]
        if len(signal_union) == 6:
            number_mapping[5] = signal
        else:
            number_mapping[2] = signal

    return number_mapping

def calculate_digits(input):

    mapping = determine_mapping(input)

    # pprint(mapping)

    work_number = ''
    for digit in input["output"]:
        # print(digit)
        for number in mapping:
            if mapping[number] == digit:
                work_number += str(number)
    # print(int(work_number))
    return int(work_number)


@click.command()
@click.argument('inputfile', type=click.File('r'))
def driver(inputfile):

    print(f"{digits=}")
    print(f"{num_lines=}")

    uniq_line_nums = []

    for num_line in num_lines:
        if len(num_lines[num_line]) == 1:
            uniq_line_nums.append(num_line)
    
    print(f"Unique number of lines for numbers: {uniq_line_nums}")

    # inputs = [line.strip().split('|')[1] for line in inputfile.readlines()]
    inputs = [] 
    for line in inputfile.readlines():
        signals = line.split('|')[0].strip().split(' ')
        output = line.split('|')[1].strip().split(' ')
        inputs.append({
            "signals": [set(signal) for signal in signals],
            "output": [set(number) for number in output],
        })
    # print(inputs)
    print(f"Found {len(inputs)} inputs to process.")

    final_sum = 0
    for input in inputs:
        digits_display = calculate_digits(input)
        # print(f"{digits_display=}")
        final_sum += digits_display

    print(f"{final_sum=}")
    # uniq_num_segments = count_segments(inputs["output"], uniq_line_nums)
    # print(f"{uniq_num_segments=}")


if __name__ == "__main__":
    driver()