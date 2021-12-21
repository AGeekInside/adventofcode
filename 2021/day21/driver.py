import click

from icecream import ic

def read_input(inputfile):

    lines = [line.strip() for line in inputfile.readlines()]

    ic(lines)

    gamestate = {
        'players': [], 
    }
    for i, line in enumerate(lines):
        player_num = i+1
        name = f'p{player_num}'
        player = {}
        location = line.split(':')[1].strip()
        player['name'] = name
        player['loc'] = int(location)
        player['score'] = 0
        gamestate['players'].append(player)

    gamestate['is_over'] = False

    return gamestate

def is_game_over(gamestate):
    for player in gamestate['players']:
        if player['name'] in ['p1', 'p2']:
            if player['score'] >= 1000:
                player['winner'] = True
                return True
    return False


class FixedDie:

    def __init__(self, last_roll=0) -> None:
        self.last_roll = last_roll 
        self.times_rolled = 0

    def roll(self):
        if self.last_roll == 100:
            new_roll = 1
        else: 
            new_roll = self.last_roll+1
        self.last_roll = new_roll
        self.times_rolled += 1
        return new_roll

FIXED_DIE = FixedDie()

def take_turn(player, num_rolls = 3):

    rolls = []

    for _ in range(num_rolls):
        rolls.append(FIXED_DIE.roll())
    # ic(rolls)

    for roll in rolls:
        player['loc'] += roll
        if player['loc'] > 10:
            remainder = player['loc'] % 10
            if remainder == 0:
                player['loc'] = 10
            else:
                player['loc'] = remainder
    # ic(player)
    player['score'] += player['loc'] 

    print(f'Player {player["name"]} roles {"+".join(str(roll) for roll in rolls)} and moves to space {player["loc"]} for a total score of {player["score"]}.')

@click.command()
@click.argument('inputfile', type=click.File('r'))
def driver(inputfile):

    gamestate = read_input(inputfile)

    gamestate['is_over'] = is_game_over(gamestate)

    ic(gamestate)

    turn = 0
    while not gamestate['is_over']:
        print(f"{turn=}")
        for player in gamestate['players']:
            # ic(player)
            take_turn(player)
            gamestate['is_over'] = is_game_over(gamestate)
            if gamestate['is_over']:
                break
            # ic(player)
        turn += 1        
        # ic(gamestate)
        # if turn > 165:
            # break

    print(f"{FIXED_DIE.times_rolled=}")
    ic(gamestate)

    puzzle_out = 0
    for player in gamestate['players']:
        if 'winner' in player:
            pass
        else:
            puzzle_out = FIXED_DIE.times_rolled * player['score']

    ic(puzzle_out)



if __name__ == "__main__":
    driver()