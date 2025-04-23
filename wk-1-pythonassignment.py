def simple_calculator():
    # Input: Read two numbers and the operation
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("Enter the operation (+, -, *, /): ")

    # Operations dictionary to map symbols to functions
    operations = {
        '+': num1 + num2,
        '-': num1 - num2,
        '*': num1 * num2,
        '/': num1 / num2 if num2 != 0 else "Error: Division by zero is not allowed."
    }

    # Get and print the result
    result = operations.get(operation, "Invalid operation. Please use one of the following: +, -, *, /.")
    if isinstance(result, str):
        print(result)
    else:
        print(f"{num1} {operation} {num2} = {result}")


# Call the function to run the calculator
simple_calculator()
