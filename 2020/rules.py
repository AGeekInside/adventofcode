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
        if not outer_color in outer_colors:
            outer_colors[outer_color] = {
                "contains": [],
                "contain_counts": {}
            }
        # print(f"outer_split: {outer_split}")
        inner_split = inner_split.strip()
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
            if not color in outer_colors[outer_color]["contains"]:
                outer_colors[outer_color]["contains"].append(color)
                outer_colors[outer_color]["contain_counts"][color] = num

        # for outer_color_to_add in outer_colors:
        #     colors_to_add = outer_colors[outer_color_to_add]["contains"]
        #     for outer_to_check in outer_colors:
        #         if outer_color_to_add in outer_colors[outer_to_check]["contains"]:
        #             outer_colors[outer_to_check]["contains"].extend(colors_to_add)
        #             outer_colors[outer_to_check]["contains"] = list(set(outer_colors[outer_to_check]["contains"]))

    # pprint(outer_colors)

    can_contain_count = 0
    for outer_color in outer_colors:
        if target_bag in outer_colors[outer_color]["contains"]:
            # print(outer_color)
            can_contain_count += 1

    print(f"Can contain: {can_contain_count}")
        
        

if __name__ == "__main__":
    main()
