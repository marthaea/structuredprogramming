total_number_of_votes = int(input("Please input the total number of votes:  "))

candidate_a = int(input("Please input the total number of votes candidate A received:  "))
candidate_b = int(input("Please input the total number of votes candidate B received: "))

candidate_ap = candidate_a/total_number_of_votes*100
candidate_bp = candidate_b/total_number_of_votes*100

print(f"The percentage votes for candidate a is {candidate_ap}% and the percentage votes for candidate b is {candidate_bp}%")
print("Thank you for voting")

#NUMBER 2
candidate1 = int(input("Please enter the number of votes for candidate 1:  "))
candidate2 = int(input("Please enter the number of votes for candidate 2:  "))

if candidate1 > candidate2:
    print("Candidate 1 wins! ")
else:
    print("Candidate 2 wins! ")
    
    
#NUMBER 3
ages1 = int(input("Enter the age of a member of parliament: "))
ages2 = int(input("Enter the age of another member of parliament: "))
ages3 = int(input("Enter the age of another member of parliament: "))
sum_a = ages1 + ages2 + ages3
average = sum_a/3
print(f"The average number of members of Uganda's parliament is {average}")

#NUMBER 4
user_age = int(input("Please input your age: "))

if user_age >= 18:
    print("You are eligible to vote, choose wisely ")
else:
    print("Unfortunately you are not yet eligible to vote. Try again in other coming years ")
    
#NUMBER 5
seats = int(input("Please enter the total number of seats: "))
party1 = int(input("Please enter the percentage of votes for party1: "))
party2 = int(input("Please enter the percentage of votes for party2: "))

if party1 > party2:
    print("Party one gets more seats")
else:
    print("Party2 gets more seats: ")
    
#NUMBER 6
party_seats = int(input("Please enter the number of seats held by the party: "))
total_number_of_seats = int(input("Please input the total number of seats: "))

percentage_required = 50/total_number_of_seats*100
percentage_of_seats = party_seats/total_number_of_seats*100

if percentage_of_seats > percentage_required:
    print("The party given is the majority in Uganda's parliament ")
else:
    print("The party given is the minority in Uganda's parliament")