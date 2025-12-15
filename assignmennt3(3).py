# Program to count vowels, consonants, and calculate ratio
def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count

def count_consonants(text):
    vowels = "aeiouAEIOU"
    consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    count = 0
    for char in text:
        if char in consonants and char not in vowels:
            count += 1
    return count

def calculate_ratio(vowels_count, consonants_count):
    if consonants_count == 0:
        return 0 # Avoid division by zero
    return vowels_count / consonants_count

# User input and output
input_string = input("Enter a string: ")
v_count = count_vowels(input_string)
c_count = count_consonants(input_string)
ratio = calculate_ratio(v_count, c_count)

print(f"Vowels: {v_count}")
print(f"Consonants: {c_count}")
print(f"Ratio (Vowels/Consonants): {ratio:.2f}")