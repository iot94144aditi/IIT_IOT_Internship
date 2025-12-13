num = int(input("Enter a 5 digit number: "))
temp = num
rev = 0

while num > 0:
    digit = num % 10 #last digit lsb
    rev = rev * 10 + digit #reversed number digit by digit
    num = num // 10 #removes last digit msb --- // used for removing the decimal part

if temp == rev:
    print("Palindrome number")
else:
    print("Not a palindrome number")