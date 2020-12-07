import hashlib
from pprint import pprint
import re

import click
from tqdm import tqdm


@click.command()
@click.argument("inputfile")
def main(inputfile):

    print(f"Reading {inputfile}")
    with open(inputfile, "r") as f:
        raw_rules = [line.strip() for line in f.readlines()]

    print(f"Found {len(raw_rules)} rule(s) to process.")

    target_bag = "shiny gold"
    outer_colors = {}
    for raw_rule in tqdm(raw_rules):
        outer_split, inner_split = raw_rule.split("contain")
        outer_split = outer_split.split("bags")[0].strip()
        outer_color = outer_split
        outer_colors[outer_color] = {
            "name": outer_color,
            "can_contain": [],
            "sub_contain": [],
            "contain_counts": {}
        }

    for raw_rule in tqdm(raw_rules):
        outer_split, inner_split = raw_rule.split("contain")
        outer_split = outer_split.split("bags")[0].strip()
        outer_color = outer_split
        # print(f"outer_split: {outer_split}")
        inner_split = inner_split.strip()
        raw_contains = []
        if inner_split == "no other bags.":
            # print(raw_rule)
            pass
        elif "," in inner_split:
            raw_contains = [raw_contain.strip() for raw_contain in inner_split.split(",")]
            # print(raw_contains)
        else:
            raw_contains = [inner_split]
            # print(raw_contains)
        
        for raw_contain in raw_contains:
            work_color = raw_contain.split("bag")[0].strip()
            num = work_color[0]
            color = work_color[2:]
            # print(work_color)
            # print(f"num: {num}, color: {color}")
            if not color in outer_colors[outer_color]["can_contain"]:
                outer_colors[outer_color]["can_contain"].append(color)
                outer_colors[outer_color]["contain_counts"][color] = num

    # pprint(outer_colors)
    for process_color in sorted(outer_colors.keys()):
        # print("**********************")
        # print(f"Checking for [{process_color}]...")
        for check_color in sorted(outer_colors.keys()):
            check_contains = outer_colors[check_color]["can_contain"]
            if not process_color == check_color:
                # print(f"Checking in [{check_color}] - {check_contains}...")
                if process_color in check_contains:
                    # print(f"---------> FOUND {process_color}")
                    # print(f"---------> [{process_color}] found in {check_contains}")
                    colors_to_add = outer_colors[process_color]["can_contain"]
                    if len(colors_to_add) > 0:
                        # print(f"----------> need to add {colors_to_add} to {check_contains}")
                        check_contains.extend(colors_to_add)
                        # print(f"check_contains: {check_contains}")
                        check_contains = list(set(check_contains))
                

    # pprint(outer_colors)

    can_contain_count = 0
    for outer_color in outer_colors:
        if target_bag in outer_colors[outer_color]["can_contain"]:
            # print(outer_color)
            can_contain_count += 1

    print(f"Can hold {target_bag}: {can_contain_count}")

    # pprint(outer_colors)
    
    contained_count = count_contents(outer_colors[target_bag], outer_colors) - 1

    print(f"{target_bag} contains {contained_count}")


def count_contents(target_bag, bags):
    print("************")
    print(target_bag)
    bag_contents = target_bag["contain_counts"]
    print(bag_contents)
    contained_bags = 1
    for contained_bag_color in bag_contents:
        bag_count = int(bag_contents[contained_bag_color])
        content_count = count_contents(bags[contained_bag_color], bags)
        contained_bags = contained_bags + (bag_count * content_count)
    
    print(f"{target_bag} contains {contained_bags} bag(s).")
    return contained_bags



if __name__ == "__main__":
    main()
