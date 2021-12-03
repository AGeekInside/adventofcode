import click
import tqdm


def calc_rating(ones_count, readings, spot, comp_func):

    # print(f"{ones_count=}")
    # print(f"{readings=}")
    # print(f"{spot=}")
    if len(readings) == 1:
        return readings
    else:
        num_readings = len(readings)
        one_count = ones_count[spot]
        zero_count = num_readings - ones_count[spot]
        value_to_use = comp_func(one_count, zero_count) 
        # print(f"{num_readings=}")
        # print(f"{one_count=}")
        # print(f"{zero_count=}")
        # print(f"{value_to_use=}")
        # print("*******************")
        filtered_readings = []
        for reading in readings:
            if reading[spot] == value_to_use:
                filtered_readings.append(reading)

        return calc_rating(count_ones(filtered_readings), filtered_readings, spot+1, comp_func)

def ox_comp_func(one_count, zero_count):
    if one_count >= zero_count:
        return '1'
    else:
        return '0'

def calc_ox_rating(ones_count, readings):
    start_spot = 0
    ox_rating = calc_rating(ones_count, readings, start_spot, ox_comp_func)
    return ox_rating

def co2_comp_func(one_count, zero_count):
    if zero_count <= one_count:
        return '0'
    else:
        return '1'

def calc_co2_rating(ones_count, readings):
    # print("STARTING CO2 RATING CALC")

    start_spot = 0
    co2_rating = calc_rating(ones_count, readings, start_spot, co2_comp_func)
    return co2_rating

def count_ones(readings):
    ones_count = [0] * (len(readings[0])-1)

    for reading in readings:
        for spot, value in enumerate(reading.strip()):
            if value == '1':
                ones_count[spot] += 1

    return ones_count

def process_readings(readings):

    gamma_rate = 0
    epsilon_rate = 0
    num_readings = len(readings)

    ones_count = count_ones(readings)

    gamma_rate = []
    epsilon_rate = []

    for spot, count in enumerate(ones_count):
        one_count = count
        zero_count = num_readings - count
        if one_count > zero_count:
            gamma_rate.append("1")
            epsilon_rate.append("0")
        else:
            gamma_rate.append("0")
            epsilon_rate.append("1")

    gamma_rate = int('0b' + ''.join(gamma_rate), 2)
    epsilon_rate = int('0b' + ''.join(epsilon_rate), 2)
    # print(ones_count)

    ox_gen_rating = int('0b' + calc_ox_rating(ones_count, readings)[0], 2)
    co2_gen_rating = int('0b' + calc_co2_rating(ones_count, readings)[0], 2)
    rates = {
        "gamma_rate": gamma_rate,
        "epsilon_rate": epsilon_rate,
        "ox_gen_rating": ox_gen_rating,
        "co2_gen_rating": co2_gen_rating,
    }
    return rates

@click.command()
@click.argument('inputfile', type=click.File('r'))
def plot(inputfile):

    readings = inputfile.readlines()
    # readings = [reading.strip() for reading in readings]

    print(f"Found {len(readings)} reading(s).")

    rates = process_readings(readings)

    print(f"{rates=}")
    # print(f'{rates["gamma_rate"]=}')
    # print(f'{rates["epsilon_rate"]=}')
    power_consumption = rates["gamma_rate"] * rates["epsilon_rate"]
    life_support = rates["ox_gen_rating"] * rates["co2_gen_rating"]
    print(f"{power_consumption=}")
    print(f"{life_support=}")


if __name__ == "__main__":
    plot()