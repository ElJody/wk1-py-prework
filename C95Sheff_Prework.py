# Question 1
# Write a function to print "hello_USERNAME!" USERNAME is the input of the function. 
# The first line of the code has been defined as below. 
# def hello_name(user_name):
def hello_name(user_name):
    print("Hello_"+user_name)
user_name = input('Enter USERNAME: ')
hello_name(user_name)


# Question 2
# Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing 
# def first_odds():
def first_odd():
    for i in range(1,101):
        if i % 2 != 0:
            print(i)
first_odd()


# Question 3
# Please write a Python function, max_num_in_list to return the max number of a given list.
# The first line of the code has been defined as below. 
# def max_num_in_list(a_list):
def max_num_in_list(a_list):
    maximum = a_list[0]
    for i in range(len(a_list)):
        if a_list[i] > maximum:
            maximum = a_list[i]
    return maximum
a_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(max_num_in_list(a_list))


# Question 4
# Write a function to return if the given year is a leap year.
# A leap year is divisible by 4, but not divisible by 100 unless it is also divisible by 400.
# The return should be boolean Type (true/false).
# def is_leap_year(a_year):
def is_leap_year(a_year):
    # Is the year is divisible by 400?
    if(a_year % 400 == 0):
        return True
    # Is the year divisible by 100? 
    # If Yes, then it is
    # It is NOT a leap year
    elif a_year % 100 == 0:
        return False
    # Is the year is divisible by 4?
    elif a_year%4 == 0:
        return True
    # Otherwise False
    else:
        return False
# Asking for user to enter year 
a_year = int(input())
# Print result of user input
print(is_leap_year(a_year))


# Question 5
# Write a function to check to see if all numbers in the list are consecutive numbers.
# For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers.
# The return should be boolean Type. def is_consecutive(a_list):
def is_consecutive(a_list):
    return sorted(a_list) == list(range(min(a_list), max(a_list)+1))
a_list = [2,3,4,5,6,7]
print(is_consecutive(a_list))
a_list = [1,2,4,5]
print(is_consecutive(a_list))

