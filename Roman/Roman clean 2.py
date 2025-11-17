def int_to_roman(n: int) -> str:
    """Convert integer to Roman numerals (supports 1..3999)."""
    # Check if the number is within the valid range
    if not (1 <= n <= 3999):
        raise ValueError("Value must be between 1 and 3999")

    # List of tuples containing values and their corresponding Roman symbols
    val_sym = [
        (1000, "M"), (900, "CM"),
        (500, "D"), (400, "CD"),
        (100, "C"), (90, "XC"),
        (50, "L"), (40, "XL"),
        (10, "X"), (9, "IX"),
        (5, "V"), (4, "IV"),
        (1, "I"),
    ]

    result = []  # List to hold the resulting Roman numeral parts
    for value, symbol in val_sym:
        if n == 0:  # Exit if no value remains to convert
            break
        count, n = divmod(n, value)  # Get quotient and remainder
        if count:  # If count is greater than 0, append the symbol
            result.append(symbol * count)  # Repeat symbol count times
    return "".join(result)  # Join the list into a single string


def main():
    try:
        # Prompt user for input and remove leading/trailing whitespace
        s = input("Enter a number (1-3999): ").strip()
        num = int(s)  # Convert input string to an integer
        roman = int_to_roman(num)  # Convert the integer to Roman numeral
    except ValueError as e:  # Handle invalid input
        print("Invalid input:", e)  # Print error message
        return  # Exit the function

    # Print the result in a formatted string
    print(f"{num} -> {roman}")


if __name__ == "__main__":
    main()  # Run the main function if the script is executed directly