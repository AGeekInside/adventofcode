import click


def process_commands(commands):

    location = {
        "horizontal": 0,
        "depth": 0,
    }
    
    location_part2 = {
        "horizontal": 0,
        "depth": 0,
        "aim": 0,
    }

    for command in commands:
        instruction, count = command.split(" ")
        count = int(count)
        match instruction:
            case "forward":
                location["horizontal"] += count
                location_part2["horizontal"] += count
                location_part2["depth"] += (count * location_part2["aim"])
            case "up":
                location["depth"] -= count
                location_part2["aim"] -= count
            case "down":
                location["depth"] += count
                location_part2["aim"] += count
            
    return location, location_part2


@click.command()
@click.argument('inputfile', type=click.File('r'))
def plot(inputfile):

    commands = inputfile.readlines()

    print(f"Found {len(commands)} command(s).")

    location, location_part2 = process_commands(commands)

    print(f"{location=}")
    print(f"{location_part2=}")

    print(f"Answer 1: {location['horizontal'] * location['depth']}")
    print(f"Answer 2: {location_part2['horizontal'] * location_part2['depth']}")

if __name__ == "__main__":
    plot()