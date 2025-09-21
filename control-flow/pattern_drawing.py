# pattern_drawing.py

# Prompt user for input
size = int(input("Enter the size of the pattern: "))

# Initialize row counter
row = 0

# Use a while loop for rows
while row < size:
    # Use a for loop for columns
    for col in range(size):
        print("*", end="")  # print * without moving to new line
    print()  # move to next line after finishing a row
    row += 1


