import statistics

import click
from icecream import ic

starters = ['(', '[', '{', '<']

closers = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>',
}

closer_value = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137,
}

def complete_input(state):
    # ic(state)

    needed_closers = []
    for starter in reversed(state["seen_starters"]):
        needed_closers.append(closers[starter])

    # ic(needed_closers)

    score = 0
    for closer in needed_closers:
        score = score * 5
        match closer:
            case ')': 
                score += 1
            case ']':
                score += 2
            case '}':
                score += 3
            case '>':
                score += 4

    return [score, needed_closers]
    

def process_input(input):

    valid = True
    result = None

    state = {
        "in_chunk": False,
        'expected_closer': '',
        'seen_starters': [],
        'input': input,
    }

    incomplete_lines = []
    for entry in input:
        if entry in starters:
            state["seen_starters"].append(entry)
            state["in_chunk"] = True
            state["expected_closer"] = closers[entry]
        elif entry in closers.values():
            if entry == state["expected_closer"]:
                state["seen_starters"].pop()
                if len(state["seen_starters"]) > 0:
                    state["expected_closer"] = closers[state["seen_starters"][-1]]
                else:
                    state["in_chunk"] = False
                    state["expectect_closer"] = ''
            else:
                # print("Closer incorrect.")
                # ic(state)
                # ic(entry)
                return False, closer_value[entry]
        else:
            print("Entry not starter or closer.")
            # ic(entry)
            return False, None
        # ic(state) 
    # ic(state)
    if state["in_chunk"]:
        score, closers_needed = complete_input(state)
        return False, [score, closers_needed]
    else:
        return valid, result

def process_inputs(inputs):

    results = []

    for input in inputs:
        validity, result = process_input(input)
        result = {
            "input": input, 
            "valid": validity,
            "result": result
        }
        # ic(result)
        results.append(result)

    return results


@click.command()
@click.argument('inputfile', type=click.File('r'))
def driver(inputfile):

    inputs = [line.strip() for line in inputfile.readlines()]

    # ic(inputs)

    results = process_inputs(inputs)

    error_score = 0
    incompletes = []
    scores = []
    for result in results:
        if not result["valid"]:
            if not isinstance(result["result"], list):
                # ic(result)
                error_score += result["result"]
            else:
                incompletes.append(result)
                scores.append(result["result"][0])

    scores = sorted(scores)
    ic(error_score)
    # ic(scores)
    ic(statistics.median(scores))

if __name__ == "__main__":
    driver()