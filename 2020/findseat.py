import copy

import click

def find_range(command, work_range):
    # print(f"In find_range")
    # print(f"command: {command}")
    # print(f"work_range: {work_range}")

    new_range = work_range
    num_in_range = work_range[1] - work_range[0]
    # print(f"num_in_range: {num_in_range}")

    if command in ["B", "R"]:
        upper = True
    else:
        upper = False

    half = (work_range[1] - work_range[0]) / 2
    # print(f"half: {half}")
    if upper:
        new_upper = work_range[1]
        new_lower = work_range[0] + half
    else:
        new_upper = work_range[1] - half
        new_lower = work_range[0] 
    
    # print(f"new_upper: {new_upper}")
    # print(f"new_lower: {new_lower}")

    new_range = (new_lower, new_upper)
    return new_range

def find_seat(boarding_pass, row_num=128, col_num=8):
    row_commands = boarding_pass[0:-3]
    seat_commands = boarding_pass[-3:]

    # print(boarding_pass)
    # print(row_commands)
    # print(seat_commands)

    work_row = 0
    work_col = 0

    work_range = (0, row_num)
    for command in row_commands:
        # print("-------------")
        work_range = find_range(command, work_range)
    work_row = work_range[0]

    work_range = (0, col_num) 
    for command in seat_commands:
        work_range = find_range(command, work_range)
    work_col = work_range[0]

    # print(f"computed row: {work_col}")
   
    # print("-------------")
    return work_row, work_col    

@click.command()
@click.argument("inputfile")
def main(inputfile):

    print(f"Reading {inputfile}")
    with open(inputfile, "r") as f:
        passes = f.read().splitlines()

    num_rows = 128
    seats_in_row = 8

    seats = [[0 for _ in range(8)] for _ in range(128)]

    max_id = 0
    id_list = []
    for boarding_pass in passes:
        row, column = find_seat(boarding_pass)
        seat_id = (row *8) + column
        seats[int(row)][int(column)] = seat_id
        id_list.append(seat_id)
        if seat_id > max_id:
            max_id = seat_id
        print(f"{boarding_pass}: row {row}, column {column}, seat ID {seat_id}")

    print(f"max seat_id = {max_id}")

    missing_seats = []
    for j, row in enumerate(seats):
        for i, col in enumerate(row):
            if col == 0:
                missing_id = ((j*8) + i) * 1.0
                missing_seats.append((j, i, missing_id))

    # for row in seats:
    #     print(row)
    print(f"found {len(missing_seats)} empty seats.")

    # print(sorted(id_list))
    print(missing_seats)
    my_seats = []
    for empty_seat in missing_seats:
        # print(empty_seat)
        plus_one = empty_seat[2] + 1
        minus_one = empty_seat[2] - 1
        # print(plus_one)
        if not plus_one in id_list:
            pass
        elif not minus_one in id_list:
            pass
        else:
            my_seats.append(empty_seat)

    print(my_seats)

if __name__ == "__main__":
    main()
