for i in range(1,101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)


def score_letter(score):
    if score >= 90:
        return "A"
    elif score >= 75:
        return "B"
    elif score >= 65:
        return "C"
    elif score >= 50:
        return "D"
    elif score >= 39:
        return "E"
    else:
        return "F"
score = float(input("Enter your numerical score from 1 to 100: "))
print("Your score letter is,",  score_letter(score))

def multiplication_table(num):
    for i in range(1,num + 1):
        print(f"{num} * {i} = {num * i}")
num = int(input("Enter any number from 1 to 10: "))
print("This is the multiplicatio table for the number: ", multiplication_table(num))

string1 = input("Enter a string: ")
string2 = input("Enter another string: ")
if string2 in string1:
    print("subString found! ")