import sys

import click
import tqdm

def cost_to_move(loc, crab_locs):

    current_cost = 0
    for crab_loc in crab_locs:
        # current_cost += abs(crab_loc - loc)
        distance = abs(crab_loc - loc)
        current_cost += (distance/2)*(distance+1)

    return current_cost


@click.command()
@click.argument('inputfile', type=click.File('r'))
def driver(inputfile):

    crab_locs = [int(location) for location in inputfile.readline().strip().split(',')]

    first_loc = min(crab_locs)
    last_loc = max(crab_locs)
    print(crab_locs)
    print(f"Found {len(crab_locs)} crab(s).")
    print(f"{first_loc=}")
    print(f"{last_loc=}")

    potential_spot = last_loc + 1
    minimum_cost = sys.maxsize
    minimum_spot = last_loc + 1
    for potential_spot in tqdm.tqdm(range(first_loc, last_loc+1)):
        current_cost = cost_to_move(potential_spot, crab_locs)
        if current_cost < minimum_cost:
            minimum_cost = current_cost
            minimum_spot = potential_spot

    print(f"{minimum_cost=}")
    print(f"{minimum_spot=}")


if __name__ == "__main__":
    driver()