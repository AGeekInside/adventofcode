import hashlib

import click
from tqdm import tqdm

def is_nice(word):
    pass

@click.command()
@click.argument("inputfile")
def main(inputfile):

    print(f"Reading {inputfile}")
    with open(inputfile, 'r') as f:
        words = f.read().splitlines()

    print(f"Found {len(words)} word(s) to check.")

    nice_words = []
    naughty_words = [] 
    for i, word in enumerate(words):
        if is_nice(word):
            nice_words.append(word)
        else:
            naughty_words.append(word)

    print(f"Nice: {nice_words}")
    print(f"Naughty: {naughty_words}")


if __name__ == "__main__":
    main()