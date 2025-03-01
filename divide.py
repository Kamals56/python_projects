#function for dividing
def divide_two_numbers(a, b):
    """Function to divide a by b, with error handling for division by zero"""
    if b == 0:
        return "Error: Division by zero is not allowed"
    else:
        return a / b