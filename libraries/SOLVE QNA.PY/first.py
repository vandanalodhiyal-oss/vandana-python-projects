num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

operation = input ("enter operation (+, _, *, /):")

if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    result = num1 / num2

print("Result:", result)