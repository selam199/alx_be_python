# Prompt the user for the size of the pattern
size = int(input("Enter the size of the pattern: "))

# Validate input (size must be a positive integer)
if size <= 0:
    print("Please enter a positive integer.")
else:
    # Initialize row counter for the while loop
    row = 0
    
    # Outer while loop for rows
    while row < size:
        # Inner for loop for columns
        for col in range(size):
            print("*", end="")  # Print asterisk without newline
        print()  # Move to the next line after finishing a row
        row += 1

