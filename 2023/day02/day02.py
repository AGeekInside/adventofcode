import click
from icecream import ic


def parse_game_info(raw_cube_info):
    cube_info = {
        "draw_colors": [],
        "color_totals": {
            "red": 0,
            "green": 0,
            "blue": 0,
        },
        "color_max": {
            "red": 0,
            "green": 0,
            "blue": 0,
        },
    }

    for cube_draw in raw_cube_info:
        cube_color = {
            "red": 0,
            "green": 0,
            "blue": 0,
        }

        draw_colors = [_.strip() for _ in cube_draw.split(",")]
        # ic(draw_colors)
        for draw_color in draw_colors:
            count, color = draw_color.split(" ")
            cube_color[color] = int(count)
            if cube_color[color] > cube_info["color_max"][color]:
                cube_info["color_max"][color] = int(count)
            cube_info["color_totals"][color] += int(count)

        cube_info["draw_colors"].append(cube_color)

    # ic(cube_info)
    return cube_info


def parse_game(line):
    # ic(line)

    raw_game_id, raw_cube_info = [x.strip() for x in line.split(":")]

    game_id = raw_game_id.split(" ")[1]

    raw_cube_info = [x.strip() for x in raw_cube_info.split(";")]

    # ic(game_id, raw_cube_info)

    game_info = []

    for cube_info in raw_cube_info:
        game_info.append(parse_game_info(raw_cube_info))

    # ic(game_info)
    return game_id, game_info


def calculate_power_sum(games_info):
    power_sum = 0
    for game_id, game_info in games_info:
        # ic(game_info)
        game_power = (
            game_info[0]["color_max"]["red"]
            * game_info[0]["color_max"]["green"]
            * game_info[0]["color_max"]["blue"]
        )
        power_sum += game_power

    return power_sum


def check_games(games_info):
    red_max = 12
    green_max = 13
    blue_max = 14

    possible_games = []

    ic("STARTING CHECK")
    for game_id, game_info in games_info:
        # ic(game_id, game_info)
        for cube_info in game_info:
            # ic(cube_info)
            if cube_info["color_max"]["red"] > red_max:
                # ic("red check", game_id, cube_info)
                break
            if cube_info["color_max"]["green"] > green_max:
                # ic("green check", game_id, cube_info)
                break
            if cube_info["color_max"]["blue"] > blue_max:
                # ic("blue check", game_id, cube_info)
                break
            possible_games.append(int(game_id))
    possible_games = set(possible_games)
    # ic(possible_games)

    games_sum = sum(possible_games)

    # ic(games_sum)

    power_sum = calculate_power_sum(games_info)
    ic(power_sum)


@click.command()
@click.argument("inputfile", type=click.File("r"))
def driver(inputfile):
    games_info = []
    for line in inputfile:
        games_info.append(parse_game(line.strip()))

    # ic(games_info)

    check_games(games_info)


if __name__ == "__main__":
    driver()
