import click

@click.command()
@click.argument("inputfile")
def main(inputfile):

    print(f"Reading {inputfile}")
    with open(inputfile, 'r') as f:
        instructions = f.read()

    print(f"Found {len(instructions)} instruction(s).")

    houses_visited = {(0,0): 1}
    current_location = [0,0]
    for instruction in instructions:
        if instruction == '^':
            current_location = [current_location[0]+1, current_location[1]]
        elif instruction == 'v':
            current_location = [current_location[0]-1, current_location[1]]
        elif instruction == '<':
            current_location = [current_location[0], current_location[1]-1]
        elif instruction == '>':
            current_location = [current_location[0], current_location[1]+1]
        else:
            print(f"Unrecognized instruction: {instruction}")
        
        house_address = (current_location[0], current_location[1])
        if not house_address in houses_visited:
            houses_visited[house_address] = 1
        else:
            houses_visited[house_address] += 1

    # print(houses_visited)

    print(f"Houses visited: {len(houses_visited.keys())}")
    
if __name__ == "__main__":
    main()