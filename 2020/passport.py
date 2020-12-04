import hashlib
import re

import click
from tqdm import tqdm


def is_num(value, required_length):
    if len(value) > required_length:
        return False
    elif len(value) < required_length:
        return False
    elif value.isdigit():
        return True
    else:
        return False


def valid_num(entry, minimum, maximum, length=4):
    if is_num(entry, length):
        if int(entry) >= minimum and int(entry) <= maximum:
            return True
    return False


def is_valid(entry):
    # expected_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"]
    expected_fields = [
        "byr",
        "iyr",
        "eyr",
        "hgt",
        "hcl",
        "ecl",
        "pid",
    ]

    valid = True

    for field in expected_fields:
        if not field in entry:
            return False

    invalid_fields = []
    year_entries = [["byr", 1920, 2002], ["iyr", 2010, 2020], ["eyr", 2020, 2030]]

    for year_entry in year_entries:
        work_field = year_entry[0]
        value = entry[work_field]
        valid = valid_num(value, year_entry[1], year_entry[2], length=4)
        if not valid:
            # print(f"{year_entry[0]}: {value} is invalid.")
            invalid_fields.append(work_field)
            valid = False

    ecl = entry["ecl"]

    if not ecl in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
        # print(f"hcl: {hcl} is invalid")
        invalid_fields.append("ecl")
        valid = False

    pid = entry["pid"]
    if not is_num(pid, 9):
        # print(f"pid: {pid} is invalid.")
        invalid_fields.append("pid")
        valid = False

    hcl = entry["hcl"]
    letter_pattern = re.compile("[a-f0-9]+")
    if hcl.startswith('#'):
        work_hcl = hcl[1:]
        if not len(work_hcl) == 6:
            invalid_fields.append("hcl")
            valid = False
        elif letter_pattern.fullmatch(work_hcl) is None: 
            invalid_fields.append("hcl")
            valid = False
    else:
        invalid_fields.append("hcl")
        valid = False

    hgt = entry["hgt"]
    if hgt.endswith("cm"):
        num = hgt[:-2]
        if not valid_num(num, 150, 193, length=3):
            invalid_fields.append("hgt")
            valid = False
    elif hgt.endswith("ft"):
        num = hgt[:-2]
        if not valid_num(num, 59, 76, length=2):
            invalid_fields.append("hgt")
            valid = False
    else:
        invalid_fields.append("hgt")
        valid = False

        

    # if len(invalid_fields) > 0:
        # print("------------------------")
        # print(invalid_fields)
        # print(entry)
    return valid


def create_passport(lines):
    # print(lines)
    new_passport = {}
    for line in lines:
        entries = line.split(" ")
        for entry in entries:
            # print(entry)
            pair = entry.split(":")
            new_passport[pair[0]] = pair[1]

    # print(new_passport)
    return new_passport


def read_passports(f):

    passports = []

    work_lines = []
    for line in f.readlines():
        input = line.strip()
        if len(input) == 0:
            new_passport = create_passport(work_lines)
            passports.append(new_passport)
            work_lines = []
        else:
            work_lines.append(line.strip())

    if len(work_lines) > 0:
        passports.append(create_passport(work_lines))

    return passports


@click.command()
@click.argument("inputfile")
def main(inputfile):

    print(f"Reading {inputfile}")
    with open(inputfile, "r") as f:
        passports = read_passports(f)

    print(f"Found {len(passports)} passport(s) to check.")

    valid_passports = []
    invalid_passports = []
    for i, passport in enumerate(passports):
        if is_valid(passport):
            valid_passports.append(passport)
        else:
            invalid_passports.append(passport)

    print(f"Valid count: {len(valid_passports)}")
    print(f"Invalid count: {len(invalid_passports)}")


if __name__ == "__main__":
    main()
