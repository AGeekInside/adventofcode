import click
from icecream import ic

class ReactorCore:
    
    def __init__(self, min=-50, max=50):
        self.min = min
        self.max = max

@click.command()
@click.argument('inputfile', type=click.File('r'))
def driver(inputfile):


    pass


if __name__ == "__main__":
    driver()
