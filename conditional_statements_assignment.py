#Number 2
secret_number = 20
attempts = 0
print("Hello, welcome to the number guessing game! ")
while True:
    user_guess = int(input("Guess a number: "))
    attempts += 1
    if user_guess <= secret_number and user_guess >= 1:
        print(f"well guessed in {attempts} attempts")
        break
    elif user_guess < secret_number:
        print("Too low, try again ")
    else:
        print("Too high try again")
    

#Number 4
word = input("Enter a word: ")
reversed_word = word[::-1]
print(f"The reversed word is {reversed_word}")

#Number 8
number = int(input("Enter a number: "))
print("Multiplication table for", number)
print("....................................")
for i in range (1,11):
    print(f"{number} * {i} = {number * i}")
    
#Number 12
string = (input("Enter a string: "))
lowercase = 0
uppercase = 0
for char in string:
    if char.islower():
        lowercase += 1
    elif char.isupper:
        uppercase += 1
        
print("Number of lowercase letters:", lowercase)
print("Number of uppercase letters:", uppercase)

#Number 13
import re
def validate_password(password):
    if not re.search("[A-Z]", password):
        return False
    
    if not re.search("[a-z]", password):
        return False
    
    if not re.search("[0-9]", password):
        return False
    
    if not re.search("[%&$]", password):
        return False
    
    if len(password) < 8 or len(password) > 16:
        return False
    return True
password = input("Enter password: ")
if validate_password(password):
    print("Password is valid! ")
else:
    print("Password is not valid. Please try again")
    input("Enter password")
    
#Number 39
number = float(input("Enter a number: "))
if number > 0:
    print("The number is positive. ")
elif number < 0:
    print("The number is negative. ")
else:
    print("The number is zero")
    
#number 50
for i in range(10):
    pattern = ""
    for j in range(i + 1):
        pattern += str(j)
    print(pattern)
    
#number41
def sum_three_numbers(a, b, c):
    total = a + b + c
    if 25 <= total <= 35:
        return 35
    else:
        return total
    
print(sum_three_numbers(10, 10, 5))
print(sum_three_numbers(10, 15, 5))
print(sum_three_numbers(10, 20, 5))
print(sum_three_numbers(10, 25, 5))

#Number 1
numbers = [i for i in range(2000, 3201) if i % 8 == 0 ]
print(numbers)

print()

#Number 6
for i in range(11):
    if i == 4 or i == 8:
        continue
    print(i)