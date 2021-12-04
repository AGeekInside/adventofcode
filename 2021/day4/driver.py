import click

from pprint import pprint


WINNERS = []


def process_raw(raw_board, board_number):

    board = []
    total = 0
    for row in raw_board:
        if len(row) > 0:
            board.append(row.split())
    for row in board:
        for item in row:
            total += int(item)
    return {
        "board_number": board_number,
        "board": board,
        "total": total,
        "marked": {
            "cols": [0]*5,
            "rows": [0]*5,
            "numbers": [],
            "total": 0,
        }
    }

def read_boards(inputfile):

    done = False
    boards = []
    board_number = 0
    while inputfile.readline():  
        raw_board = [next(inputfile).strip() for _ in range(5)]
        if raw_board == '':
            break
        if raw_board:
            boards.append(process_raw(raw_board, board_number))
            board_number += 1

    return boards

def mark_board(draw, board):

    for row_num, row in enumerate(board["board"]):
        for col_num, value in enumerate(row):
            if value == draw:
                board["marked"]["rows"][row_num] += 1
                board["marked"]["cols"][col_num] += 1
                board["marked"]["numbers"].append(draw)
                board["marked"]["total"] += int(draw)



def check_for_win(draw, board):

    if ((5 in board["marked"]["rows"]) or (5 in board["marked"]["cols"])):
        if not board["board_number"] in WINNERS:
            board["final_score"] = int(draw) * (board["total"] - board["marked"]["total"])
            WINNERS.append(board)
        return True
    else:
        return False


def draw_numbers(draws, boards):

    have_win = False
    for draw in draws:
        for board in boards:
            if not board in WINNERS:
                mark_board(draw, board)
                have_win = check_for_win(draw,board)


@click.command()
@click.argument('inputfile', type=click.File('r'))
def main(inputfile):

    draws = inputfile.readline().strip().split(",")

    print(f"Found {len(draws)} draw(s).")

    boards = read_boards(inputfile)

    draw_numbers(draws, boards)

    pprint(WINNERS[-1])

if __name__ == "__main__":
    main()
