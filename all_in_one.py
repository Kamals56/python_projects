
# Define the functions
def add_two_numbers(a, b):
    """Function to add two numbers"""
    return a + b

def subtract_two_numbers(a, b):
    """Function to subtract b from a"""
    return a - b

def divide_two_numbers(a, b):
    """Function to divide a by b, with error handling for division by zero"""
    if b == 0:
        return "Error: Division by zero is not allowed"
    else:
        return a / b

# Main part of the script
print("Using addition")
x = add_two_numbers(1, 2)
print("1 + 2 = " + str(x))

print("\nUsing subtraction")
y = subtract_two_numbers(5, 3)
print("5 - 3 = " + str(y))

print("\nUsing division")
z = divide_two_numbers(10, 2)
print("10 / 2 = " + str(z))

# Example of division by zero
z_zero = divide_two_numbers(10, 0)
print("10 / 0 = " + str(z_zero))
