import os

def main():

    for dir_suffix in range(1, 26):
        dir_prefix = "day"
        directory = f"{dir_prefix}{dir_suffix:02d}"
        print(directory)

        # create the directory
        #os.mkdir(directory)

        # copy driver.py to the directory and rename it to main.py
        os.system(f"cp driver.py {directory}/{directory}.py")

        # copy input.txt to the directory
        os.system(f"touch {directory}/input.txt")

        # copy test_input.txt to the directory
        os.system(f"touch {directory}/test_input.txt")

        # copy test_output.txt to the directory
        os.system(f"touch {directory}/test_output.txt")

if __name__ == "__main__":
    main()