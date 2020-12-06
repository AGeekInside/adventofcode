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
        forms = [line.strip() for line in f.readlines()]

    print(forms)

    groups = []

    work_group = []
    work_form = None
    for form in forms:
        work_form = form
        # print(work_form)
        if len(form) == 0:
            # print(f"new group")
            groups.append(work_group)
            work_group = []
        else:
            work_group.append(form)

    groups.append(work_group) 
    # print(groups)
    
    group_infos = []
    for group in groups:
        print(f"{group} has size {len(group)}")
        group_info = {
            "size": len(group),
            "yes_count": 0,
            "all_yes_count": 0,
        }
        group_answers = {}
        for answers in group:
            for answer in answers:
                if answer in group_answers:
                    group_answers[answer] += 1
                else:
                    group_answers[answer] = 1
        group_info["answers"] = group_answers
        group_info["yes_count"] = len(group_answers.keys())
        for answer in group_info["answers"]:
            if group_info["answers"][answer] == group_info["size"]:
                group_info["all_yes_count"] += 1
        group_infos.append(group_info)

    pprint(group_infos)

    total = 0
    all_total = 0
    for group_info in group_infos:
        total += group_info["yes_count"]
        all_total += group_info["all_yes_count"]
    print(f"Sum of the yes counts: {total}")
    print(f"Sum of the all yes counts: {all_total}")

if __name__ == "__main__":
    main()
