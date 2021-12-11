from dataclasses import dataclass
from typing import List

import click
from icecream import ic

@dataclass
class EnergyLevels:
    states: List[List[int]]
    step: int = 0


def blank_state(initial_value):
    return [[initial_value for _ in range(10)] for _ in range(10)] 

def read_state(input_file):
    initial_state = EnergyLevels(states=blank_state(0))
    
    for row, line in enumerate(input_file.readlines()):
        for column, level in enumerate(line.strip()):
            initial_state.states[row][column] = int(level)

    ic(initial_state)

    return initial_state

def find_flashing(state):
    nines = []
    for row in range(10):
        for col in range(10):
            if state.states[row][col] > 9:
                nines.append((row, col))

    return nines

def find_adj(cell):
    row = cell[0]
    col = cell[1]

    adj = []

    first_row = row == 0
    last_row = row == 9
    first_col = col == 0
    last_col = col ==9

    if first_row and first_col:
        adj.append((row+1, col+1))
        adj.append((row, col+1))
        adj.append((row+1, col))
        return adj

    if first_row and last_col:
        adj.append((row, col-1))
        adj.append((row+1, col-1))
        adj.append((row+1, col))

    if last_row and first_col:
        adj.append((row-1,col))
        adj.append((row-1,col+1))
        adj.append((row,col+1))

    if last_row and last_col:
        adj.append((row-1, col-1))
        adj.append((row, col-1))
        adj.append((row-1, col))
        return adj

    if (not last_row) and first_col:
        adj.append(())
        return adj

    if (not last_row) and last_col:
        adj.append((row-1, col-1))
        adj.append((row+1, col-1))
        adj.append((row, col-1))
        adj.append((row-1, col))
        adj.append((row+1, col))
        return adj

    if (not first_row) and first_col:
        return adj

    if (not first_row) and last_col:
        return adj

    if first_row and (not first_col):
        return adj
    
    if last_row and (not first_col):
        return adj
        
    if first_row and (not last_col):
        return adj

    if last_row and (not last_col):
        adj.append((row, col+1))
        adj.append((row, col-1))
        adj.append((row-1, col-1))
        adj.append((row-1, col))
        adj.append((row-1, col+1))
        return adj


def flash(to_flash, state, flashed):
    ic(to_flash)

    row = to_flash[0]
    col = to_flash[1]

    adj_cells = find_adj(to_flash)

    ic(adj_cells)

def process_step(state, step):
    if state.step >= step:
        print("Error with the state step value.")
        ic(state)
        ic(step)

    flashed = [] 

    # add 1 to every entry
    for row in range(10):
        for col in range(10):
            state.states[row][col] += 1

    # find all the nines
    flashing = find_flashing(state)
    # if len(flashing) > 0:
    #     ic(flashing)

    for to_flash in flashing:
        if not to_flash in flashed:
            flash(to_flash, state, flashed)


@click.command()
@click.argument('inputfile', type=click.File('r'))
@click.argument('num_steps', type=click.INT) 
def driver(inputfile, num_steps):

    state = read_state(inputfile)

    for step in range(1, num_steps+1):
        ic(step)
        process_step(state, step)

    # ic(state)

if __name__ == "__main__":
    driver()