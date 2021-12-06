from collections import defaultdict
from pprint import pprint
from typing import KeysView

import click
import tqdm

def output_pop(work_pop):

    line = ""
    for key in sorted(work_pop):
        line += f"{work_pop[key]}:{key}, "

    print(line) 

def simulate_day(work_pop):

    # pprint(work_pop)
    new_pop = work_pop.copy()
    # print("before changes")
    # output_pop(new_pop)
    for key in range(8, -1, -1):
        match key:
            case 8:
                new_pop[7] = work_pop[8]
            case 7:
                new_pop[6] = work_pop[7]
            case 6:
                new_pop[5] = work_pop[6]
            case 5:
                new_pop[4] = work_pop[5]
            case 4:
                new_pop[3] = work_pop[4]
            case 3:
                new_pop[2] = work_pop[3]
            case 2:
                new_pop[1] = work_pop[2]
            case 1:
                new_pop[0] = work_pop[1]
            case 0:
                new_pop[8] = work_pop[0]
                new_pop[6] += work_pop[0]
    
    # print("after changes")
    # output_pop(new_pop)
    #     if key == 0:
    #         new_pop[6] = work_pop[key] + work_pop[7]
    #         new_pop[8] = work_pop[key]  
    #     elif not key == 7:
    #         if work_pop[key] > 0:
    #             new_pop[key-1] = work_pop[key]

    for new_key in range(7, -1, -1):
        if new_key < 5:
            # print(f"{new_key=}")
            # output_pop(work_pop)
            # output_pop(new_pop)
            # print(f"{work_pop[new_key+1]=}")
            # print(f"{new_pop[new_key]=}")
            # print(f"checking {new_key}")
            # print(f"{work_pop[new_key+1]} == {new_pop[new_key]}")
            assert work_pop[new_key+1] == new_pop[new_key]

    return new_pop


@click.command()
@click.argument('inputfile', type=click.File('r'))
@click.argument('days', type=int)
def driver(inputfile, days):

    initial_pop = inputfile.readline().strip().split(',')

    current_pop = defaultdict(int)
    # print(f"{initial_pop=}")

    for fish in initial_pop:
        current_pop[int(fish)] +=1

    print("Initial state")
    output_pop(current_pop)

    for day in tqdm.tqdm(range(days)):
        # print("Before:")
        # output_pop(current_pop)
        current_pop = simulate_day(current_pop)
        # print("After:")
        # output_pop(current_pop)
        # print("*"*8)
        ages = ""
        pop_count = 0
        for age in sorted(current_pop):
            ages += f"[{age}]->{current_pop[age]} "
            pop_count += current_pop[age]
        # print(f"{ages=}")
        # print(f"{pop_count=}")
    #    print(f"After {day+1} day(s):  {current_pop}") 

    pprint(current_pop)
    pop_count = 0
    for key in current_pop:
        pop_count += current_pop[key]
    print(f"Sum: {pop_count}")

if __name__ == "__main__":
    driver()