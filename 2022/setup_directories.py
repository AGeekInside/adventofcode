import os

def main():

    for dir_suffix in range(1, 26):
        dir_prefix = "day"
        directory = f"{dir_prefix}{dir_suffix:02d}"
        print(directory)

        # create the directory
        os.mkdir(directory)
    

if __name__ == "__main__":
    main()