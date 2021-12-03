import click
import tqdm

def calc_ox_rating(ones_count, readings):

    num_readings = len(readings)

    for spot, one_count in enumerate(ones_count):
        zero_count = num_readings - one_count
        print(f"{zero_count=}")
        print(f"{one_count=}")
        print(f"{num_readings=}")

def calc_c02_rating(ones_count, readings):

    pass 

def process_readings(readings):

    gamma_rate = 0
    epsilon_rate = 0
    num_readings = len(readings)

    ones_count = [0] * (len(readings[0])-1)

    for reading in readings:
        for spot, value in enumerate(reading.strip()):
            if value == '1':
                ones_count[spot] += 1

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
    print(ones_count)

    ox_gen_rating = calc_ox_rating(ones_count, readings)
    co2_gen_rating = calc_c02_rating(ones_count, readings)
    rates = {
        "gamma_rate": gamma_rate,
        "epsilon_rate": epsilon_rate,
        "ox_gen_rating": ox_gen_rating,
        "c02_gen_rating": co2_gen_rating,
    }
    return rates

@click.command()
@click.argument('inputfile', type=click.File('r'))
def plot(inputfile):

    readings = inputfile.readlines()

    print(f"Found {len(readings)} reading(s).")

    rates = process_readings(readings)

    print(f'{rates["gamma_rate"]=}')
    print(f'{rates["epsilon_rate"]=}')
    power_consumption = rates["gamma_rate"] * rates["epsilon_rate"]
    print(f"{power_consumption=}")


if __name__ == "__main__":
    plot()