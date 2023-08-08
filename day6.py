# DAY 6
# Advanced topics in Python 
"""
- Regular expressions
- Generators and iterators
- Decorators
- Context managers
- Multithreading and multiprocessing
"""

#Regular expressions
#Summary 
"""
- Regular expressions are used to match patterns in strings.
- Regular expressions can be used to match patterns in strings.
 
"""

# Matching and Searching
# regex re.march(),re.search(), re.findall()

# # Example1 Demonstration regex | Match First Word, Match Group word, Match All Numbers 
# import re
# text = "Hello, my name is Ariho Conrad, I am a programmer with 2 years of experience"

# # Match First Word 
# match = re.search(r"\b\w+\b", text)

# if match:
#     print("Match: ", match.group())

# matches = re.findall(r"\d+", text)
# print("Match: ", matches)


# # Example2 validate email format or email address 
# import re 

# def validate_email(email):
#     pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
#     if re.search(pattern, email):
#         return True
#     else:
#         return False

# #Example usage 
# email1 =  "arihoconrad3@gmail.com"
# email2 = "geof.anthony@gmail.com"

# print(validate_email(email1))
# print(validate_email(email2))

# Generators and Iterators
# 'yeild' generator
# Iterator '__iter__' "__next__" iterator 

# def factorial(n):
#     # return the factorial of a number
#     if n == 0:
#         yield 1 
#     else:
#         fact = 1

#     for i in range(1, n+1):
#         fact *= i 
#         yield fact 

# # Print the factorial of a number from 1 - 10
# for i in range(1,10):
#     print(factorial(i))

# Example 3 

# Generate function that yields the square of numbers from 1-10

def squares():
    for i in range(1, 10):
        yield i ** 2
        
# Create an iterator object that yields the sqaure of numbers from 1-10

squares_iterator = squares()

# Print the first 5 squares of numbers from 1 to 10
for i in range(5):
    print(next(squares_iterator)) 

# Decorators @mydecorator

def my_decorator(func):
    def inner():
        print("This is the decorator")
        func()
    return inner

@my_decorator
def outer_decorator(func):
    print("This is outer decorator")

outer_decorator()










































