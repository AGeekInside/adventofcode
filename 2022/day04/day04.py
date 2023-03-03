import click
from icecream import ic

def parse_assignment(assignment):
    start, end = assignment.split("-")

    return {
        "start": int(start),
        "end": int(end),
    }

def parse_assignment_pair(line):
    first_assignment, second_assignment = line.split(",")

    first_assignment = parse_assignment(first_assignment)
    second_assignment = parse_assignment(second_assignment)

    return {
        "first_assignment": first_assignment,
        "second_assignment": second_assignment,
    }

def read_assignments(inputfile):
    assignments = []
    for line in inputfile:
        assignments.append(parse_assignment_pair(line))
    return assignments

@click.command()
@click.argument('inputfile', type=click.File('r'))
def driver(inputfile):

    assignments = read_assignments(inputfile)

    print(assignments)

if __name__ == "__main__":
    driver()
