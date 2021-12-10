from pprint import pprint

import click
from icecream import ic


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

    low_points = []
    risk_levels = [] 
    for i, row in enumerate(heightmap["map"]):
        # print(f"{row=}")
        for j, value in enumerate(row):
            is_lowest = True
            if j > 0:
                if row[j-1] <= value:
                    is_lowest = False
            if j < heightmap["width"] - 1:
                if row[j+1] <= value:
                    is_lowest = False
            if i > 0:
                if heightmap["map"][i-1][j] <= value:
                    is_lowest = False
            if i < heightmap["depth"] - 1:
                if heightmap["map"][i+1][j] <= value:
                    is_lowest = False
            if is_lowest:
                risk_levels.append(value+1)
                low_points.append((i, j))

    heightmap["low_points"] = low_points
    heightmap["risk_levels"] = risk_levels
    return risk_levels
            

def find_basin(location, current_basin, heightmap):
    row = location[0]
    column = location[1]
    location_value = heightmap["map"][row][column]

    if location in current_basin:
        return
    if location_value == 9:
        return
    else:
        current_basin.append(location)
        if column > 0:
            find_basin((row, column-1), current_basin, heightmap)
        if column < heightmap["width"] - 1:
            find_basin((row, column+1), current_basin, heightmap)
        if row > 0:
            find_basin((row-1, column), current_basin, heightmap)
        if row < heightmap["depth"] - 1:
            find_basin((row+1, column), current_basin, heightmap)


def find_basins(heightmap):

    chasms = []

    for low_point in heightmap["low_points"]:
        current_basin = []
        find_basin(low_point, current_basin, heightmap)
        chasms.append({
            "basin": current_basin,
            "size": len(current_basin),
        })

    sorted_chasms = sorted(chasms, key = lambda i: i['size'], reverse=True)
    return sorted_chasms
    

@click.command()
@click.argument('inputfile', type=click.File('r'))
def driver(inputfile):
    heightmap = read_map(inputfile)

    risk_levels = find_risk_levels(heightmap)

    print(f"Sum of risk: {sum(risk_levels)}")

    basins = find_basins(heightmap)

    answer = basins[0]["size"] * basins[1]["size"] * basins[2]["size"] 

    ic(answer)


if __name__ == "__main__":
    driver()