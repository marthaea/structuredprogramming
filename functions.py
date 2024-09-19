#no 1
#A python program to find the maximum number in a list
def max_num(a,b,c):
    return max(a, b, c)
a = 3
b = 7
c = 9
print("The maximum number is; ", max_num(a, b, c))

#no 2
#the sum of all numbers in a list
def sum_of_items_in_list(item):
    return sum(items)
items = [4,67,93,0,2]
print("The sum of items in a list is: ", sum_of_items_in_list(items))

#no 4
# A python program to reverse a string
string = "Martha"
reversed_string = string[::-1]
print("Original string:", string, "and the reversed string:", reversed_string )

#no 6
#a python program to check wheather a number falls within a certain range
def check_range(num,lower,upper):
    if lower <= num <= upper:
        print(f"{num} falls within range [{lower},{upper}]")
    else:
        print(f"{num} doesnot fall within range [{lower},{upper}]")
check_range(5, 1, 10)

#no 17
#a python function to detect a function inside a function
def outer_function():
    def inner_function():
        return "Hello from inner function!"
    return inner_function()
print(outer_function())