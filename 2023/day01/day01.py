import click
import re

from icecream import ic


@click.command()
@click.argument("inputfile", type=click.File("r"))
def driver(inputfile):
    calibration_values = []
    # Dictionary to map spelled out numbers to integers
    number_map = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
    }

    exception_list = {
        "oneight": ["1", "8"],
        "twone": ["2", "1"],
        "threeight": ["3", "8"],
        "fiveight": ["5", "8"],
        "sevenine": ["7", "9"],
        "eightwo": ["8", "2"],
        "eighthree": ["8", "3"],
        "nineight": ["9", "8"],
    }

    for line in inputfile:
        line = line.strip()

        ic(line)
        # Assuming 'line' is your string

        numbers = re.findall(
            r"\d|oneight|twone|threeight|fiveight|sevenine|eightwo|eighthree|nineight|one|two|three|four|five|six|seven|eight|nine",
            line,
        )
        ic(numbers)

        # Convert spelled out numbers to integers
        new_numbers = []
        for n in numbers:
            if n in number_map:
                new_numbers.append(str(number_map[n]))
            elif n in exception_list:
                new_numbers.extend(exception_list[n])
            else:
                new_numbers.append(n)
        numbers = new_numbers
        ic(numbers)

        if len(numbers) < 2:
            calibration_value = numbers[0] + numbers[0]
        else:
            calibration_value = numbers[0] + numbers[-1]

        ic(calibration_value)
        calibration_values.append(int(calibration_value))

        # ic(calibration_values)

    # Summing the calibration_values
    total_calibration = sum(calibration_values)
    ic(len(calibration_values))
    ic(total_calibration)


if __name__ == "__main__":
    driver()
