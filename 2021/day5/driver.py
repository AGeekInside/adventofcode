from collections import defaultdict
from pprint import pprint

import click


def read_coord(raw_coord):

    return {
        "x_coord": int(raw_coord.split(',')[0].strip()),
        "y_coord": int(raw_coord.split(',')[1].strip()),
    }


def mark_line(vent_line, vent_locations):

    if vent_line["type"] == "horizontal":
        start_x = min(vent_line["start_coord"]["x_coord"], vent_line["end_coord"]["x_coord"])
        end_x = max(vent_line["start_coord"]["x_coord"], vent_line["end_coord"]["x_coord"])
        work_y = vent_line["start_coord"]["y_coord"]
        for mark_x in range(start_x, end_x+1):
            vent_locations[(mark_x, work_y)] += 1
    elif vent_line["type"] == "vertical":
        start_y = min(vent_line["start_coord"]["y_coord"], vent_line["end_coord"]["y_coord"])
        end_y = max(vent_line["start_coord"]["y_coord"], vent_line["end_coord"]["y_coord"])
        work_x = vent_line["start_coord"]["x_coord"]
        for mark_y in range(start_y, end_y+1):
            vent_locations[(work_x, mark_y)] += 1
    elif vent_line["type"] == "diagonal":
        if vent_line["x_delta"] < 0:
            x_coords = range(vent_line["start_coord"]["x_coord"], vent_line["end_coord"]["x_coord"]-1, -1)
        else:
            x_coords = range(vent_line["start_coord"]["x_coord"], vent_line["end_coord"]["x_coord"]+1)
        if vent_line["y_delta"] < 0:
            y_coords = range(vent_line["start_coord"]["y_coord"], vent_line["end_coord"]["y_coord"]-1, -1)
        else:
            y_coords = range(vent_line["start_coord"]["y_coord"], vent_line["end_coord"]["y_coord"]+1)
        coords = zip(x_coords, y_coords)
        for coord in coords:
            vent_locations[coord] += 1


def process_line(vent_line, vent_locations):

    raw_start_coord, raw_end_coord = vent_line.split(" -> ")

    start_coord = read_coord(raw_start_coord)
    end_coord = read_coord(raw_end_coord)

    vent_line = {
        "start_coord": start_coord,
        "end_coord": end_coord,
        "x_delta": end_coord["x_coord"] - start_coord["x_coord"],
        "y_delta": end_coord["y_coord"] - start_coord["y_coord"],
    }

    if ((not vent_line["x_delta"] == 0) and (not vent_line["y_delta"] == 0)):
        vent_line["type"] = "diagonal"
    elif not vent_line["x_delta"] == 0:
        vent_line["type"] = "horizontal"
    else:
        vent_line["type"] = "vertical"

    mark_line(vent_line, vent_locations)


def process_input(inputfile):

    vent_locations = defaultdict(int)

    vent_lines = inputfile.readlines()

    print(f"Found {len(vent_lines)} vent lines.")

    for vent_line in vent_lines:
        process_line(vent_line, vent_locations)

    return vent_locations

@click.command()
@click.argument('inputfile', type=click.File('r'))
def driver(inputfile):

    vent_locations = process_input(inputfile)

    count = 0
    for location in vent_locations:
        if vent_locations[location] > 1:
            count += 1

    print(f"Found {count} locations with > 1 overlap.")


if __name__ == "__main__":
    driver()