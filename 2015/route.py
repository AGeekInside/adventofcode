import click

def update_location(instruction, current_loc):
    new_loc = None
    if instruction == '^':
        new_loc = (current_loc[0]+1, current_loc[1])
    elif instruction == 'v':
        new_loc = (current_loc[0] - 1, current_loc[1])
    elif instruction == '<':
        new_loc = (current_loc[0], current_loc[1]-1)
    elif instruction == '>':
        new_loc = (current_loc[0], current_loc[1]+1)
    else:
        print(f"Unrecognized instruction: {instruction}")

    return new_loc
        

@click.command()
@click.argument("inputfile")
def main(inputfile):

    print(f"Reading {inputfile}")
    with open(inputfile, 'r') as f:
        instructions = f.read()

    print(f"Found {len(instructions)} instruction(s).")

    santa_houses = {(0,0): 1}
    robo_houses = {(0,0): 1}
    santa_loc = (0,0)
    robo_loc = (0,0)

    for i, instruction in enumerate(instructions):
        if (i % 2) == 0:
            santa_loc = update_location(instruction, santa_loc)
            house_address = santa_loc
            if not house_address in santa_houses:
                santa_houses[house_address] = 1
            else:
                santa_houses[house_address] += 1
        else:
            robo_loc = update_location(instruction, robo_loc)
            house_address = robo_loc
            if not house_address in robo_houses:
                robo_houses[house_address] = 1
            else:
                robo_houses[house_address] += 1


    print(santa_houses)
    print(robo_houses)

    houses = [house for house in santa_houses.keys()]
    houses.extend([house for house in robo_houses.keys()])
    houses = set(houses)
    total_visits = len(houses)
    print(f"Houses visited: {total_visits}")
    
if __name__ == "__main__":
    main()