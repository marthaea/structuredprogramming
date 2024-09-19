print("Hello welcome to 'Knowing God' ")
print("We're so glad we get to have you here! God loves you!! ")
print("Praise the name of God")
print("Now enter your name")

name_user = (input("Please enter your name: "))
print(f"Hello {name_user}! What a beautiful name you have!")
print(f"{name_user}, Have you ever given your life to Jesus Christ? ")
print("1. No. but I would like to give it a try ")
print("2. Yes but I backslid later on ")
print("3. Yes! ")
print("4. No! ")
answer = int(input("Please enter option according to your response: "))

if answer == 1:
    print("That is wonderful! Please proceed and give us your mail. We can always communicate with you and pray for you")
elif answer == 2:
    print("God is willing to have you back! Please enter your email...")
elif answer == 3:
    print("Praise God! Please share your mail for daily devotion and encouragement ")
else:
    print("Jesus loves you, our dear friend. Kindly give us your email...")
    
import re
def username_validator(username):
    pattern = r'^[a-zA-Z][a-zA-Z0-9]{2,15}$'
    if re.match(pattern, username):
        return True
    return False

def password_validator(usermail,password,username):
    if len(password) < 8:
        return False
    if len(usermail) < 5:
        return False
    if len(username) > 7:
        return False
usermail = input("Kindly enter your email")
userpassword = input("Great, now set your password: ")
username = input("Enter your username: ")
print(f"HELLO {username}")
print(f"{usermail}")
print("You are now fully registered for the app. Now enjoy our exclusive serices as well as knowing more about God")
