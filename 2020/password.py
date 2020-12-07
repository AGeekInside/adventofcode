import hashlib

import click
from tqdm import tqdm


def is_valid(entry):
    rule, password = entry.split(":")
    password = password.strip()
    range, required_char = rule.split(" ")
    minimum, maximum = range.split("-")
    minimum = int(minimum)
    maximum = int(maximum)

    count = 0

    check_locs = [minimum - 1, maximum - 1]

    count = 0
    for loc in check_locs:
        # print(f"Checking {loc} of {password} for {required_char}")
        if password[loc] == required_char:
            # print(f"Found it")
            count += 1

    if count == 1:
        return True
    else:
        return False

    # if ((count >= minimum) and (count <= maximum)):
    #     return True
    # else:
    #     return False


@click.command()
@click.argument("inputfile")
def main(inputfile):

    print(f"Reading {inputfile}")
    with open(inputfile, "r") as f:
        entries = f.read().splitlines()

    print(f"Found {len(entries)} word(s) to check.")

    valid_passwords = []
    invalid_passwords = []
    for i, entry in enumerate(entries):
        if is_valid(entry):
            valid_passwords.append(entry)
        else:
            invalid_passwords.append(entry)

    print(f"Valid count: {len(valid_passwords)}")
    print(f"Invalid count: {len(invalid_passwords)}")


if __name__ == "__main__":
    main()
