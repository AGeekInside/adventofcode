import click
from icecream import ic

@click.command()
@click.argument('inputfile', type=click.File('r'))
def driver(inputfile):

    pass


if __name__ == "__main__":
    driver()
