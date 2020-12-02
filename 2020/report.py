import click


@click.command()
@click.argument("inputfile")
def process_report(inputfile):

    print(f"Reading {inputfile}")
    with open(inputfile, "r") as f:

        entries = f.read().splitlines()

    entries = [int(entry) for entry in entries]

    done = False
    for outer in entries:
        for middle in entries[1:]:
            for inner in entries[2:]:
                work_sum = outer + middle + inner
                if work_sum == 2020:
                    print(f"{outer} + {middle} + {inner} = 2020")
                    print(f"product is {outer * middle * inner}")
                    done = True
                    break
            if done:
                break
        if done:
            break


if __name__ == "__main__":
    process_report()
