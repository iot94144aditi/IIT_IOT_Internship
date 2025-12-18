# --- arithmetic functions ---
def add(a, b):
    """Returns the sum of a and b."""
    return a + b

def multiply(a, b):
    """Returns the product of a and b."""
    return a * b

# --- string operation functions ---
def reverse_string(s):
    """Reverses the input string."""
    return s[::-1]

def count_vowels(s):
    """Counts the number of vowels in the input string."""
    vowels = "aeiouAEIOU"
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count

# --- Main Program (demonstration logic) ---
def main ():
    print("--- Demonstrating Arithmetic Functions ---")
    num1 = 10
    num2 = 5
    # Call the functions directly since they are in the same file
    sum_result = add(num1, num2)
    product_result = multiply(num1, num2)
    print(f"Addition of {num1} and {num2}: \033[1m{sum_result}\033[0m")
    print(f"Multiplication of {num1} and {num2}: \033[1m{product_result}\033[0m")

    print("\n--- Demonstrating String Operations ---")
    test_string = "Hello World"
    # Call the functions directly since they are in the same file
    reversed_str = reverse_string(test_string)
    vowel_count = count_vowels(test_string)
    print(f"Original string: '{test_string}'")
    print(f"Reversed string: \033[1m'{reversed_str}'\033[0m")
    print(f"Number of vowels: \033[1m{vowel_count}\033[0m")

if _name_ == "_main_":
    main()