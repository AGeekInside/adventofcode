from dataclasses import dataclass, field
from typing import List

SIZE = 10

import click
from icecream import ic

@dataclass
class EnergyLevels:
    states: List[List[int]]
    step: int = 0
    num_flashes: int = 0

    def lookup_loc(self, cell):
        return self.states[cell[0]][cell[1]]


def blank_state(initial_value):
    return [[initial_value for _ in range(SIZE)] for _ in range(SIZE)] 

def read_state(input_file):
    initial_state = EnergyLevels(states=blank_state(0))
    
    for row, line in enumerate(input_file.readlines()):
        for column, level in enumerate(line.strip()):
            initial_state.states[row][column] = int(level)

    ic(initial_state)

    return initial_state

def find_flashing(state):
    to_flash = []
    for row in range(SIZE):
        for col in range(SIZE):
            if state.states[row][col] > 9:
                to_flash.append((row, col))

    return to_flash

def find_adj(cell):
    row = cell[0]
    col = cell[1]

    adj = []

    first_row = row == 0
    last_row = row == 9
    first_col = col == 0
    last_col = col ==9

    good_coords = [coord for coord in range(SIZE)]
    for horz in range(-1,2):
        for vert in range(-1,2):
            new_row = row + vert
            new_col = col + horz
            if not new_row in good_coords:
                continue
            if not new_col in good_coords:
                continue
            adj_coord = (new_row, new_col)
            if not adj_coord == cell:
                adj.append((new_row, new_col))

    return adj


def flash(to_flash, state, flashed):
    row = to_flash[0]
    col = to_flash[1]

    if to_flash in flashed:
        return
    else:
        state.states[to_flash[0]][to_flash[1]] = 0
        state.num_flashes += 1
        flashed.append(to_flash)
        adj_cells = find_adj(to_flash)

        for adj_cell in adj_cells:
            if not adj_cell in flashed:
                state.states[adj_cell[0]][adj_cell[1]] += 1
                if state.states[adj_cell[0]][adj_cell[1]] > 9:
                    flash(adj_cell, state, flashed)


def process_step(state, step):
    if state.step >= step:
        print("Error with the state step value.")
        ic(state)
        ic(step)

    flashed = [] 

    # add 1 to every entry
    for row in range(SIZE):
        for col in range(SIZE):
            state.states[row][col] += 1

    flashing = find_flashing(state)

    for to_flash in flashing:
        if not to_flash in flashed:
            flash(to_flash, state, flashed)

    state.step += 1


@click.command()
@click.argument('inputfile', type=click.File('r'))
@click.argument('num_steps', type=click.INT) 
@click.argument('size', type=click.INT, default=10) 
def driver(inputfile, num_steps, size):

    global SIZE

    SIZE = size
    ic(SIZE)
    state = read_state(inputfile)

    not_synched = True
    step=1
    # for step in range(1, num_steps+1):
    while not_synched:
        process_step(state, step)
        in_synch = True
        for row in state.states:
            for val in row:
                if val > 0:
                    in_synch = False
        
        if in_synch:
            ic(state)
            not_synched = False

        step += 1


    ic(state)
    with open("final_state.out", "w") as f:
        for row in state.states:
            out_row = ''
            for value in row:
                out_row += str(value)
            f.write(out_row+'\n')

if __name__ == "__main__":
    driver()