import click


@click.command()
@click.argument('inputfile', type=click.File('r'))
def driver(inputfile):

    crab_locs = inputfile.readline().strip().split(',')

    print(crab_locs)
    print(f"Found {len(crab_locs)} crab(s).")

    pass


if __name__ == "__main__":
    driver()