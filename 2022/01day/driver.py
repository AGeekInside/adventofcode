
def read_inputfile(inputfile):

    elves = []
    current_elf_calories = 0

    for line in inputfile:
        if len(line.strip()) > 0:
            new_food = int(line.strip())
            current_elf_calories += new_food
        else:
            elves.append(current_elf_calories)
            current_elf_calories = 0
    elves.append(current_elf_calories)
    return elves

def find_top_three(elves):
    
    top_three = [0, 0, 0]
    
    for elf in elves:
        if elf > top_three[0]:
            top_three[2] = top_three[1]
            top_three[1] = top_three[0]
            top_three[0] = elf
        elif elf > top_three[1]:
            top_three[2] = top_three[1]
            top_three[1] = elf
        elif elf > top_three[2]:
            top_three[2] = elf

    return top_three

def __main__():

    with open("input.txt", "r") as inputfile:
        elves = read_inputfile(inputfile)

    print(max(elves))

    top_three = find_top_three(elves)

    print(top_three[0] + top_three[1] + top_three[2])

if __name__ == "__main__":
    __main__()