def create_file():
    try:
        # Create a new text file named "my_file.txt" in write mode ('w')
        with open("my_file.txt", "w") as file:
            # Write at least three lines of text to the file, including a mix of strings and numbers
            file.write("My name is Stephen Kanene Muhindi.\n")
            file.write("I am an undergraduate student.\n")
            file.write("This is my file handling assignment\n")
    except (FileNotFoundError, PermissionError) as e:
        print("Error occurred while creating the file:", e)
    finally:
        print("File creation process completed.")


def read_and_display():
    try:
        # Open "my_file.txt" in read mode ('r')
        with open("my_file.txt", "r") as file:
            # Read and display the contents of the file
            print("Contents of 'my_file.txt':")
            for line in file:
                print(line.strip())
    except FileNotFoundError as e:
        print("Error occurred while reading the file:", e)


def append_to_file():
    try:
        # Open "my_file.txt" in append mode ('a')
        with open("my_file.txt", "a") as file:
            # Append three additional lines of text to the existing content
            file.write("I'm looking foward to learn more.\n")
            file.write("This is my github profile;https://github/Muhindisk.\n")
            file.write("End of the file.\n")
    except (FileNotFoundError, PermissionError) as e:
        print("Error occurred while appending to the file:", e)


def main():
    create_file()
    read_and_display()
    append_to_file()


if __name__ == "__main__":
    main()
