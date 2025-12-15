# Program using a higher-order function for arithmetic
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b

def calculate(operand1, operand2, operation_func):
    return operation_func(operand1, operand2)

# Test with different inputs and operations
num1 = 10
num2 = 15

print(f"{num1} + {num2} = {calculate(num1, num2, add)}")
print(f"{num1} - {num2} = {calculate(num1, num2, subtract)}")
print(f"{num1} * {num2} = {calculate(num1, num2, multiply)}")
print(f"{num1} / {num2} = {calculate(num1, num2, divide)}")