# Exercise 2: File Handling with FileNotFoundError

filename = input("Enter the filename to open: ")

try:
    with open(filename, "r") as file:
        content = file.read()
        print("File content:")
        print(content)
except FileNotFoundError:
    print(f"Error: The file '{filename}' does not exist.")
