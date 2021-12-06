from collections import defaultdict
from pprint import pprint

import click
import tqdm

def simulate_day(work_pop):

    pprint(work_pop)
    new_pop = work_pop.copy()
    for key in range(8, -1, -1):
        print(f"{key=}")
        print(f"{work_pop=}")
        print(f"{new_pop=}")
        if key == 0:
            new_pop[6] = work_pop[key]
            new_pop[8] = work_pop[key]  
        else:
            if work_pop[key] > 0:
                new_pop[key-1] = work_pop[key]
        print(f"{new_pop=}")

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

    pprint(current_pop)

    print(f"Initial state: {current_pop}")
    for day in tqdm.tqdm(range(days)):
        current_pop = simulate_day(current_pop)
        ages = ""
        pop_count = 0
        for age in sorted(current_pop):
            ages += f"[{age}]->{current_pop[age]} "
            pop_count += current_pop[age]
        print(f"{ages=}")
        print(f"{pop_count=}")
    #    print(f"After {day+1} day(s):  {current_pop}") 

    pprint(current_pop)
    pop_count = 0
    for key in current_pop:
        pop_count += current_pop[key]
    print(f"Sum: {pop_count}")

if __name__ == "__main__":
    driver()