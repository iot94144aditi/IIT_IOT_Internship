def greet(name="User", msg="Welcome"):
    print(msg, name)

greet()
greet("Aditi")
greet(msg="Hello", name="IoT Student")

def square(x):
    return x * x

def apply_function(func, value):
    return func(value)

print(apply_function(square, 5))
