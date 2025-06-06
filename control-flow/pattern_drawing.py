# pattern_drawing.py

# Prompt user to enter the size of the pattern
size = int(input("Enter the size of the pattern: "))

# Initialize row counter
row = 0

# Outer loop using while to handle rows
while row < size:
    # Inner loop using for to print asterisks in each row
    for _ in range(size):
        print("*", end="")
    # Move to the next line after each row
    print()
    # Increment row counter
    row += 1
