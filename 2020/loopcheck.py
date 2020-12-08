import copy 
import hashlib
from pprint import pprint
import re

import click
from tqdm import tqdm

ACCUM_VALUE = 0    

def has_loop(instructions):

    done = False
    executed_addrs = []
    steps = []
    # result_addr = {}
    termination_addr = len(instructions) - 1
    in_addr = 0
    execution_step = 0
    accum_value = 0
    
    while not done:
        current_instruction = instructions[in_addr]
        # print(f"Executing inst: [{execution_step}]-[{in_addr}] - {current_instruction}")

        new_addr, accum_value = process_inst(current_instruction, in_addr, accum_value)
        # result_addr[str(execution_step)+"-"+current_instruction] = new_addr
        # print(f"New address: {new_addr}")
        executed_addrs.append(in_addr)
        step = f"{current_instruction}  |  {new_addr}"
        steps.append(step)
        if new_addr in executed_addrs:
            print(f"Infinite loop found.")
            return True, accum_value
        elif new_addr == termination_addr:
            print(f"No loop found.")
            return False, accum_value
        if new_addr > len(instructions):
            print(f"{new_addr} invalid address. Ending")
            done = True, accum_value
        in_addr = new_addr
        execution_step += 1


@click.command()
@click.argument("inputfile")
def main(inputfile):

    print(f"Reading {inputfile}")
    with open(inputfile, "r") as f:
        raw_instructions = [line.strip() for line in f.readlines()]
        
    instructions = [[inst.split(" ")[0], int(inst.split(" ")[1])] for inst in raw_instructions]
    print(instructions)

    variations_to_check = []

    for i, instruction in enumerate(instructions):
        print(f"{i} --- {instruction}")
        print(instructions)
        new_list = copy.deepcopy(instructions)
        print(instruction)
        if instruction[0] == "nop":
            # new_list = instructions.copy()
            # print(f"Changing {new_list[i][0]} to 'jmp'.")
            new_list[i][0] = "jmp"
            variations_to_check.append(new_list)
        elif instruction[0] == "jmp":
            # new_list = instructions.copy()
            # print(f"Changing {new_list[i][0]} to 'nop'.")
            new_list[i][0] = "nop"
            variations_to_check.append(new_list)
        # pprint(variations_to_check)
    print(f"Found {len(variations_to_check)} variation(s) to check.")

    loop_present, _ = has_loop(instructions)

    if loop_present:
        print(f"Initial instructions have a loop.")
        print("Checking variations")
        for i, variation in enumerate(variations_to_check):
            print(f"-----> Checking [{i}] variation")
            pprint(variation)
            loop_present, accum_value = has_loop(variation)
            if not loop_present:
                print(f"loop_present: {loop_present}, accum_value: {accum_value}")

    # print(f"loop_present : {loop_present}")
    # print(f"Accumulated value: {accumulated_value}")


def process_inst(current_instruction, in_addr, accum_value):
    new_addr = in_addr
    inst = current_instruction[0]
    value = current_instruction[1]
    # inst, value = current_instruction.split(" ")
    # value = int(value)

    if inst == "nop":
        new_addr += 1
    elif inst == "acc":
        accum_value += value
        new_addr += 1
    elif inst == "jmp":
        new_addr += value
    return new_addr, accum_value

if __name__ == "__main__":
    main()
