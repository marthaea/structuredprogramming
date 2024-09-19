#lists
#no 1
#summing all the items in the list
def sum_list(numbers):
    total = 0
    for number in numbers:
        total += number 
    return total
numbers = [1,2,3,4,5]
print("Sum of the list:", sum_list(numbers))

#no 2
#multipling elements in the list
def multiplylistelements(elements):
    product = 1
    for element in elements:
        product *= element
    return product
elements = [11, 1, 4, 5] 
print("The product of elements in a list is: ", multiplylistelements(elements))

#no 3
#finding the largest number in the list
numbers = [12, 34, 30, 44, 56]
largestnumber = max(numbers)
print("Largest number: ", largestnumber)

#no 4
#finding the smallest number in the list
numbers = [12, 34, 30, 44, 56]
minimumnumber = min(numbers)
print("Smallest number is:", minimumnumber)

#no 7
#sorting out duplicates from the list
my_list = [1,2,2,2,2,2,5,6,3,6,3,2]
my_list = list(set(my_list))
print("List without duplicates: ", my_list)

#no 8
#checking wheather the list is empty or not
list = []
if not list:
    print("List is empty ")
else:
    print("List is not empty")
list2 = [1,4,7]
if not list2:
    print("list 2 is empty")
else:
    print("list 2 is not empty ")
    
#no 20
#turning a list into a string
char_list = ['H','e','l','l','o']
my_string = "".join(char_list)
print(my_string)

#no21
#finding the index of an item in a specified list
my_list = ['apple', 'grapes', 'oranges', 'guava']
item = 'grapes'
index = my_list.index(item)
print(f"The index of '{item}'is: {index}")

#n0 23
#selecting a random item on the list
import random
list = [1,2,3,4,5,6]
random_number = random.choice(list)
print(f"The randomly selected number is: {random_number}")

#no 24
#finding the second smallest on the list
my_list = [2,7,9,33,8]
my_list.sort()
second_smallest = my_list[1]
print(second_smallest)

#Dictionaries
#no 1
#printing the dictionary in ascending order
my_dictionary = {'apple':5, 'banana':3, 'cherry':8, 'date':2, 'strawberry':4}
asc_sorted_dict = dict(sorted(my_dictionary.items(), key = lambda item: item[1]))

print("Ascending order: ")
print(asc_sorted_dict)

desc_sorted_dict = dict(sorted(my_dictionary.items(), key = lambda item: item[1], reverse=True))
print("Descending order")
print(desc_sorted_dict)

#no 4
#iterating over dictionaries using for loops
my_dictionary = {'apple':5, 'banana':3, 'cherry':8, 'date':2, 'strawberry':4}

print("Keys:")
for key in my_dictionary:
    print(key)
print("Values")
for value in my_dictionary.values():
    print(value)
print("Items")
for key, value in my_dictionary.items():
    print(f"{key}:{value}")
    
#Turples
#no 1
#creating a turple
my_tuple = (1,2,3,4,5)
print(my_tuple)

#no 5
#adding an item on a turple
my_tuple = (1,2,3,4,5)
#turples are immutable

#sets
#no 1
#creating a set
my_set = {1,2,3,4,5,6}
print(my_set)

#no 2
#iterating over elements in a set
my_set = {1,2,3,4,5,6}
for element in my_set:
    print(element)