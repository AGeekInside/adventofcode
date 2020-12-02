import hashlib

import click
from tqdm import tqdm

def find_key(secret_key):

    start_int = 1

    done = False
    offset = 0
    batch_size = 1000000
    start_num = 1
    while not done:
        print(f"Testing: {start_num} to {start_num + batch_size}")
        for loop_num in tqdm(range(batch_size)):
            test_key = start_num + loop_num
            input_value = secret_key + str(test_key)
            hash_value = hashlib.md5(input_value.encode('utf-8')).hexdigest()
            test_portion = hash_value[:6]
            if test_portion == "000000":
                print(f"Found integer at {test_key}")
                print(f"Test portion: {test_portion}")
                done = True
                break
                print(f"MD5: {hash_value}")
        start_num += batch_size

@click.command()
@click.argument("inputfile")
def main(inputfile):

    print(f"Reading {inputfile}")
    with open(inputfile, 'r') as f:
        secret_key = f.read().strip()

    print(f"Input key: {secret_key}.")

    int_key = find_key(secret_key)

    print(f"Integer key: {int_key}")


if __name__ == "__main__":
    main()