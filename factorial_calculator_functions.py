def get_non_negative_integer() -> int:
    """
    Prompts the user to enter a non-negative integer.
    Ensures the input is a valid non-negative integer.
    
    Returns:
        int: The validated non-negative integer entered by the user.
    """
    while True:
        try:
            # Prompt the user to enter a non-negative integer
            user_input = input("Enter a non-negative integer: ")
            # Convert the input to an integer
            number = int(user_input)
            # Check if the number is non-negative
            if number >= 0:
                return number
            print("Invalid input! Please enter a non-negative integer.")
        except ValueError:
            # Handle cases where input is not a valid integer
            print("Invalid input! Please enter a valid integer.")

def calculate_factorial(n: int) -> int:
    """
    Calculates the factorial of a given non-negative integer using an iterative approach.
    
    Args:
        n (int): The non-negative integer whose factorial is to be calculated.
    
    Returns:
        int: The calculated factorial value.
    """
    if n == 0:
        return 1  # Base case: 0! = 1

    factorial = 1
    for i in range(1, n + 1):
        factorial *= i  # Multiply each number up to n

    return factorial

def main():
    # Get a valid non-negative integer from the user
    number = get_non_negative_integer()
    # Compute the factorial
    result = calculate_factorial(number)
    # Display the result
    print(f"The factorial of {number} is: {result}")

# Run the main function if the script is executed
if __name__ == "__main__":
    main()