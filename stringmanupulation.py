#NUMBER 2
#a python program to count the occurence of each character in a string
def count_times(string):
    count_times = {}
    i = 0
    while i < len(string):
        count = string[i]
        if count in count_times:
            count_times[count] += 1
        else:
            count_times[count] = 1
        i += 1
    return count_times
string = "programming"
print(count_times(string))

#NUMBER 4
#a program to concatnate and swap the first and last characters
def swap_characters(string_a, string_b):
    if len(string_a) > 1 and len(string_b) > 1:
        string_a_list = list(string_a)
        string_b_list = list(string_b)
        string_a_list[0], string_b_list[-1] = string_b[0], string_a_list[-1]
        string_b_list[0], string_a_list[-1] = string_a[0], string_a_list[-1]
        return ''.join(string_a_list), ''.join(string_b_list)
    else:
        return string_a, string_b

string_a = "Hello"
string_b = "World"
print("Original strings: string_a = {}, string_b ={}".format(string_a, string_b))
string_a, string_b = swap_characters(string_a, string_b)
print("Swapped strings: string_a = {}, string_b = {}".format(string_a, string_b))

#number 7
#a python program to remove characters at odd indeces
def remove_odd_index_characters(word):
    return word[::2]
word = input("Enter a word: ")
print("Original word: ", word)
new_word = remove_odd_index_characters(word)
print("Word after removing characters at odd indexes: ", new_word)

#Number 10
#Reverse a string
string = "Martha"
reversed_string = string[::-1]
print(f"Original string is: {string} and reversed string is: {reversed_string}")

#Number 12
#Reverse word in a string
def reverse_words_in_a_string(string):
    words = string.split()
    reverse_words_in_a_string = words[::-1]
    return " ".join(reverse_words_in_a_string)
string = input("Enter a string: ")
print("Original string: ", string)
reversed_string = reverse_words_in_a_string(string)
print("String after reversing: ", reversed_string)

#Number 16
#sum of digits in a string
def sum_of_digits(s):
    return sum(int(c) for c in s if c.isdigit())
s = input("Enter a string: ")
print("Original string: ", s)
sum_of_digits_in_s = sum_of_digits(s)
print("Sum of digits in the string: ", sum_of_digits_in_s)

#Number 18
#Count character types
def count_special_characters(s):
    special_characters = "!@#$%^&*()[]"
    count = 0 
    for char in s:
        if char in special_characters:
            count += 1
    return count
s = input("Enter a string: ")
print("Original string: ", s)
special_characters_count = count_special_characters(s)
print("Number of special characters in the string: ", special_characters_count)

#number 33
#finding all duplicate characters in a string
def find_duplicate_characters(s):
    char_count = {}
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    duplicate_characters = [char for char, count in char_count.items() if count >1]
    return duplicate_characters
s = input("Enter a string: ")
print("Original string: ", s)
duplicate_characters = find_duplicate_characters(s)
print("Duplicate charactersin the string: ", duplicate_characters)

#Number 31
#finding the second most frequent character in the string
from collections import Counter

def find_second_most_frequent_characters(s):
    char_count = Counter(s)
    char_count = sorted(char_count.items(), key = lambda x: x[1], reverse =True)
    if len(char_count) < 2:
        return None
    else:
        return char_count[1][0]
s = input("Enter a string: ")
print("Original string: ", s)
second_most_frequent_character = find_second_most_frequent_characters(s)
if second_most_frequent_character is None:
    print("There is no second most frequent character in a string")
else:
    print("Second most frequent character in a string: ", second_most_frequent_character)
    
#Number 30
#capitalize the first letter of the string
def capitalize_first_letter(s):
    return s.title()
s = input("Enter a string: ")
print("Original string: ", s)
capitalized_string = capitalize_first_letter(s)
print("String with capitalized first letter of each word: ", capitalized_string)







