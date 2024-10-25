#question 1
for i in range(1,6):
    print(i)
#question 2
i = 1
while i <= 10:
    if 1 % 2 == 0:
        print(i)
    i += 1
#question 3 
for i in range(1,4):
    for j in range(1,4):
        print(f"{i} * {j} = {i*j}")
#question 4
fruits = ['apple', 'banana', 'cherry']
for fruit in fruits:
    print(fruit)
#question 5
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
sum_of_primes = 0
i = 2
while i < 50:
    if is_prime(i):
        sum_of_primes += i
    i += 1
print(sum_of_primes)
    
#question 6
for i in range(10, 0, -1):
    print(i)
    
#7
i = 1
while i < 3:
    for i in range(1,4):
        for j in range(1,6):
            print(f"{i}* {j} = {i*j}")
print("Done")

#8 
for i in range(1, 11):
    if i % 2 == 0:
        print(i)
    i += 1
#9
num = 1
while num <= 20:
    if num % 3 != 0 and num % 5 != 0:
        print(num)
    num += 1


     
        