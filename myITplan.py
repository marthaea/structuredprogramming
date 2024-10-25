print("Welcome!")
print("There are only three possibilities for each club: 'city win','city draw', 'city loss', 'arsenal win', 'arsenal draw', 'arsenal loss,")

possibility = input("Enter any of the possibility above for Arsenal: ")
possibility = input("Enter any of the possibility above for Man City: ")
if possibility == "city win" and possibility == "arsenal loss":
    print("Man city will be crowned champions")
elif possibility == "city draw " and possibility == "arsenal win":
    print("Arsenal will be crowned champions")
elif possibility == "city draw" and possibility == "arsenal draw":
    print("Man city will be crowned champions")
else:
    print("Invalid entry")