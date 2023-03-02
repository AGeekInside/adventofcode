from pprint import pprint
import string

import click
from icecream import ic


def find_shared_items(first_component, second_component):
    shared_items = []
    for item in first_component:
        if item in second_component:
            if item not in shared_items:
                shared_items.append(item)
    return shared_items

def find_shared_in_three(first_component, second_component, third_component):
    shared_items = []
    for item in first_component:
        if item in second_component and item in third_component:
            if item not in shared_items:
                shared_items.append(item)
    return shared_items

def find_priority(item):
    priority = 0

    if item in string.ascii_lowercase:
        priority = string.ascii_lowercase.index(item) + 1 

    if item in string.ascii_uppercase:
        priority = string.ascii_uppercase.index(item) + 27

    print(f"Item: {item}, Priority: {priority}")

    return priority

def parse_rucksack(line):
    line_length = len(line)
    mid_point = line_length // 2

    first_component = line[0:mid_point]
    second_component = line[mid_point:line_length]

    shared_items = find_shared_items(first_component, second_component)

    number_of_shared_items = len(shared_items)
    # print(number_of_shared_items)

    for item in shared_items:
        priority = find_priority(item)

    return {
        "first_component": first_component,
        "second_component": second_component,
        "shared_items": shared_items,
        "priority": priority,
        "number_of_shared_items": number_of_shared_items,
        "original_line": line.strip(),
    }

def find_second_priority(rucksack_group):
    second_priority = 0

    shared_items = find_shared_in_three(
        rucksack_group[0]["original_line"],
        rucksack_group[1]["original_line"],
        rucksack_group[2]["original_line"],
    )
    print(f"Shared Items: {shared_items}")

    return find_priority(shared_items[0])

def read_rucksacks(inputfile):
    rucksacks = []
    for line in inputfile:
        rucksacks.append(parse_rucksack(line.strip()))
    return rucksacks

@click.command()
@click.argument('inputfile', type=click.File('r'))
def driver(inputfile):

    rucksacks = read_rucksacks(inputfile)

    total_priority = 0
    for rucksack in rucksacks:
        total_priority += rucksack["priority"]

    print(total_priority)

    second_priority = 0

    work_group = []
    for counter, ruksack in enumerate(rucksacks):
        # print(f"Work Group: {work_group}")
        print(f"Counter: {counter}")
        if counter % 3 == 0 and counter != 0:
            print("Found a group of 3")
            second_priority += find_second_priority(work_group)
            work_group = []
        work_group.append(ruksack)

    second_priority += find_second_priority(work_group)
    print(f"Second Priority: {second_priority}")

if __name__ == "__main__":
    driver()
