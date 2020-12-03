import copy

import click


def output_map(work_map):
    for row in work_map:
        for entry in row:
            print(entry, end="")
        print("")

def traverse_map(work_map, right_step=3, down_step=1):
    map_height = len(work_map)

    print(f"Working on a map with height {map_height} and initial width of {len(work_map[0])}")

    current_loc = (0,0)
    past_bottom = False

    traveled_map = copy.deepcopy(work_map)
    while not past_bottom:
        map_width = len(traveled_map[0])
        new_loc = (current_loc[0]+right_step, current_loc[1]+down_step)
        # print(f"Current width: {map_width}")
        # print(f"Current height: {map_height}")
        # print(f"new loc: {new_loc}")
        if new_loc[1] >= map_height:
            past_bottom = True
            # print(f"Existed map at {new_loc}")                        
            return traveled_map
        if new_loc[0] >= map_width:
            # print("{new_loc[0]} > {map_width}")
            for i, row in enumerate(traveled_map):
                row.extend(work_map[i])
        if traveled_map[new_loc[1]][new_loc[0]] == '.':
            traveled_map[new_loc[1]][new_loc[0]] = 'O'
        else:
            traveled_map[new_loc[1]][new_loc[0]] = 'X'
        current_loc = new_loc

def count_trees(work_map):
    tree_count = 0
    for row in work_map:
        for entry in row:
            if entry == 'X':
                tree_count += 1

    return tree_count 

@click.command()
@click.argument("inputfile")
def main(inputfile):

    print(f"Reading {inputfile}")
    with open(inputfile, "r") as f:
        entries = f.read().splitlines()

    start_map = [list(line) for line in entries]
    # output_map(start_map)
    # traveled_map = traverse_map(start_map)
    # output_map(new_map)

    slopes = [(1,1), (3,1), (5,1), (7,1), (1,2)]

    tree_counts = 1
    for slope in slopes:
        print(f"Checking {slope}")
        traveled_map = traverse_map(start_map, right_step=slope[0], down_step=slope[1])
        new_tree_count = count_trees(traveled_map) 
        print(f"Found {new_tree_count} tree(s).")
        tree_counts = tree_counts * new_tree_count
    
    print(f"Multiple of tree counts: {tree_counts}")

if __name__ == "__main__":
    main()
