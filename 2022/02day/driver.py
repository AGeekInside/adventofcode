
from tkinter import W

strategy_lookup = {
    ('X', 'rock'): 'scissors',
    ('X', 'paper'): 'rock',
    ('X', 'scissors'): 'paper',
    ('Y', 'rock'): 'rock',
    ('Y', 'paper'): 'paper',
    ('Y', 'scissors'): 'scissors',
    ('Z', 'rock'): 'paper',
    ('Z', 'paper'): 'scissors',
    ('Z', 'scissors'): 'rock',
}


opponent_lookup = {
    'A': 'rock',
    'B': 'paper',
    'C': 'scissors',
}

strategy = {
    'X': 'rock',
    'Y': 'paper',
    'Z': 'scissors',
}

def play_round(strategy, opponent):
    score = 0
    
    if strategy == 'rock':
        score = 1
        if opponent == 'rock':
            score += 3
        elif opponent == 'paper':
            score += 0 
        elif opponent == 'scissors':
            score += 6
    elif strategy == 'paper':
        score = 2
        if opponent == 'rock':
            score += 6
        elif opponent == 'paper':
            score += 3
        elif opponent == 'scissors':
            score += 0 
    elif strategy == 'scissors':
        score = 3
        if opponent == 'rock':
            score += 0 
        elif opponent == 'paper':
            score += 6
        elif opponent == 'scissors':
            score += 3
    print(strategy, opponent, score)
    return score

def score_strategies(strategies):
    score = 0
    for opponent, strategy in strategies:
        score += play_round(strategy, opponent) 
    return score

def read_strategy_file(strategyfile):

    strategies = []

    for line in strategyfile:
        if len(line.strip()) > 0:
            entry = line.strip().split()
            print(entry)
            opponent = opponent_lookup[entry[0].strip()]
            strategy = strategy_lookup[entry[1].strip(), opponent]
            game = opponent, strategy
            strategies.append(game)

    return strategies


def main():
    with open("input.txt", "r") as inputfile:
        strategies = read_strategy_file(inputfile)

    print(strategies)
    print(score_strategies(strategies))
    
if __name__ == "__main__":
    main()