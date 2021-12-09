from pprint import pprint

import click


def read_map(inputfile):

    map = []

    for line in inputfile.readlines():
        row = line.strip()
        cells = [int(cell) for cell in row]
        map.append(cells)

    return {
        "map": map,
        "width": len(map[0]),
        "depth": len(map)
    }


def find_risk_levels(heightmap):

    risk_levels = [] 
    for i, row in enumerate(heightmap["map"]):
        # print(f"{row=}")
        for j, value in enumerate(row):
            is_lowest = True
            # print(f"{i=}")
            # print(f"{j=}")
            # print(f"{value=}")
            if j > 0:
                # print(f"Checking if {row[j-1]} <= {value}")
                if row[j-1] <= value:
                    is_lowest = False
            if j < heightmap["width"] - 1:
                # print(f"Checking if {row[j+1]} <= {value}")
                if row[j+1] <= value:
                    is_lowest = False
            if i > 0:
                # print(f"Checking if {heightmap['map'][i-1][j]} <= {value}")
                if heightmap["map"][i-1][j] <= value:
                    is_lowest = False
            if i < heightmap["depth"] - 1:
                # print(f"Checking if {heightmap['map'][i+1][j]} <= {value}")
                if heightmap["map"][i+1][j] <= value:
                    is_lowest = False
            if is_lowest:
                risk_levels.append(value+1)

    return risk_levels
            



@click.command()
@click.argument('inputfile', type=click.File('r'))
def driver(inputfile):
    heightmap = read_map(inputfile)
    # pprint(heightmap)

    risk_levels = find_risk_levels(heightmap)
    # pprint(risk_levels)

    print(f"Sum of risk: {sum(risk_levels)}")

if __name__ == "__main__":
    driver()