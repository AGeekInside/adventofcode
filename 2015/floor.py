import click

@click.command()
@click.argument("inputfile")
def main(inputfile):

    print(f"Reading {inputfile}")
    with open(inputfile, 'r') as f:
        instructions = f.read()

    current_floor = 0

    print(f"Starting floor: {current_floor}")
    
    for i, instruction in enumerate(instructions):
        if instruction == '(':
            current_floor += 1
        if instruction == ')':
            current_floor -= 1
        if current_floor == -1:
            print(f"Instruction {i+1} caused {current_floor}")

    print(f"Final floor: {current_floor}")

if __name__ == "__main__":
    main()