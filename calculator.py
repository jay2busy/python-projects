def calculator():
    # Get user input
    num1 = float(input("Enter the first number: "))
    operator = input("Enter the operator (+, -, *, /, %): ")
    num2 = float(input("Enter the second number: "))

    # Calculate the result
    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        if num2 != 0:
            result = num1 / num2
        else:
            print("Error: Division by zero is not allowed.")
            return
    elif operator == "%":
        if num2 != 0:
            result = num1 % num2
        else:
            print("Error: Division by zero is not allowed.")
            return
    else:
        print("Error: Invalid operator.")
        return

    # Print the result
    print(f"{num1} {operator} {num2} = {result}")

# Test the calculator function
def test_calculator():
    print("Testing calculator function...")
    test_cases = [
        {"num1": 10, "operator": "+", "num2": 5},
        {"num1": 10, "operator": "-", "num2": 5},
        {"num1": 10, "operator": "*", "num2": 5},
        {"num1": 10, "operator": "/", "num2": 5},
        {"num1": 10, "operator": "%", "num2": 5},
        {"num1": 10, "operator": "/", "num2": 0},  # Test division by zero
        {"num1": 10, "operator": "%", "num2": 0},  # Test modulus by zero
        {"num1": 10, "operator": "^", "num2": 5},  # Test invalid operator
    ]

    for test_case in test_cases:
        num1 = test_case["num1"]
        operator = test_case["operator"]
        num2 = test_case["num2"]

        if operator == "+":
            result = num1 + num2
        elif operator == "-":
            result = num1 - num2
        elif operator == "*":
            result = num1 * num2
        elif operator == "/":
            if num2 != 0:
                result = num1 / num2
            else:
                result = "Error: Division by zero is not allowed."
        elif operator == "%":
            if num2 != 0:
                result = num1 % num2
            else:
                result = "Error: Division by zero is not allowed."
        else:
            result = "Error: Invalid operator."

        print(f"{num1} {operator} {num2} = {result}")

# Run the calculator function or test it
while True:
    print("1. Run calculator")
    print("2. Test calculator")
    print("3. Quit")
    choice = input("Enter your choice: ")

    if choice == "1":
        calculator()
    elif choice == "2":
        test_calculator()
    elif choice == "3":
        break
    else:
        print("Invalid choice. Please try again.")
