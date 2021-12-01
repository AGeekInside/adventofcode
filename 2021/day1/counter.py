import click


def count_increases(input):

    previous_input = None
    count = 0

    for entry in input:
        
        entry = int(entry)
        if not previous_input:
            previous_input = entry
        else:
            if entry > previous_input:
                count += 1
            previous_input = entry
    
    return count


def count_window_increases(input_numbers):
    num_window = len(input_numbers)-2 
    print(f"Found {num_window} windows.")

    window_totals = [0] * num_window

    for i, entry in enumerate(input_numbers):
        entry = int(entry.strip())
        if i == 0:
            window_totals[i] += entry
        elif i == 1:
            window_totals[i-1] += entry
            window_totals[i] += entry
        elif i ==  (num_window):
            window_totals[i-2] += entry
            window_totals[i-1] += entry
        elif i == (num_window + 1):
            print(f"Adding {entry} to {window_totals[i-2]}")
            window_totals[i-2] += entry
        else:
            window_totals[i-2] += entry
            window_totals[i-1] += entry
            window_totals[i] += entry

    print(window_totals)        

    window_increases = count_increases(window_totals)
    return window_increases


@click.command()
@click.argument('inputfile', type=click.File('r'))
def counter(inputfile):

    input_numbers = inputfile.readlines()

    print(f"Found {len(input_numbers)} input numbers.")

    increase_count = count_increases(input_numbers)
    print(f"Found {increase_count} increases.")

    windows_increases = count_window_increases(input_numbers)
    print(f"Found {windows_increases} window increases.")

if __name__ == "__main__":
    counter()