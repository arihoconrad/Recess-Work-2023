#day 3
# Basic Operators and Expressions (Input and Output operators)
"""
-Arithmetic Operators
+ Addition
- Subtraction
* Multiplication
/ Division
% Modulus
** Exponentiation

-Comparison Operators
< Less than
> Greater than
<= Less than or equal to
>= Greater than or equal to
== Equal to
!= Not equal to

-Logical Operators
Logical NOT: 'not'




-Assignment Operators
= Assignment
+= Addition and Assignment
-= Subtraction and Assignment
/= Divide and Assignment
*= Multiply and Assignment
%= Modulo and Assignment


-Membership Operators
In: 'in' operator: Checks if a value exists in a sequence 
Not in: 'not in' operator: Checks if a value does not exist in a sequence
"""

#Arithmetic Operators 
#Addition
# x = 35 + 50
# print(x)
# #Subtraction
# y = 35 - 50
# print(y)
# #Multiplication
# v = 35 * 50
# #Division
# u = 50/30
# print(u)
# #Modulo
# p = 23 % 2
# print(p)
# #Exponentiation
# z = 35 ** 2
# print(z)

# #Comparison Operators
# #Examples
# a = 16
# b = 9

# #Greater than
# if a > b:
#     print("a is greater than b")
#     print(a>b)
# #Less than
# if a < b:
#     print("a is less than b")
#     print(a<b)
# #Greater than or equal to
# if a >= b:
#     print("a is greater than or equal to b")
#     print(a<=b)
# if b >= a:
#     print("b is greater than or equal to a")
#     print(b>=a)
# #Less than or equal to
# if a <= b:
#     print("a is less than or equal to b")
#     print(a<=b)
# #Equal to
# if a == b:
#     print("a is equal to b")
#     print(a==b)
# #Not equal to
# if a != b:
#     print("a is not equal to b")
#     print(a!=b)

# #Logical Operators
# a = True
# b = False

# #Logical AND
# print(a and b)

# #Logical OR
# print(a or b)

# #Logical NOT
# print(not a)
# print(not b)

# #Assignment Operators
# # Compound assignment operators
# a = 10

# #Add and Assign 
# a += 5
# print(a) 

# #Subtract and Assign
# a -= 5
# print(a)

# #Multiply and Assign
# a *= 5
# print(a)

# #Divide and Assign
# a /= 5
# print(a)

# #Modulo and Assign
# a %= 5
# print(a)

# #Exponentiation and Assign
# a **= 5
# print(a)

# #Membership Assignment operators
# cars = ["Benz", "Jeep", "Tesla", "BMW", "RollsRoyce"]
# if 'Jeep' in cars:
#     print("Jeep is in the list")
#     print("Toyota" in cars)
#     print("RollsRoyce" in cars)

# if 'Toyota' in cars:
#     print("Toyota is in the list")
    
# #Identity assignment operators
# #List 
# #is not operator 

# z = [1, 2, 3, 4, 5]
# w = [1, 2, 3, 4, 5]

# print(z is not w)

#Bitwise operator
"""
Bitwise operators are used to perform operations on individual bits in of binary numbers

Bitwise AND (&): performs a bitwise AND operation between the corresponding bits of two integers
Bitwise OR (|): performs a bitwise OR operation between the corresponding bits of two integers
Bitwise XOR (^): performs a bitwise XOR operation 
Bitwise NOT (~): performs a bitwise NOT operation on an integer
Bitwise left shift (<<): performs a bitwise left shift operation
Bitwise right shift (>>): performs a bitwise right shift operation

"""
# #Examples of Bitwise operations
# a = 5
# b = 6

# #Bitwise AND operation
# result_and = a & b
# print(result_and)

# #Bitwise OR operation
# result_or = a | b
# print(result_or)

# #Bitwise XOR operation
# result_xor = a ^ b
# print(result_xor)

# #Bitwise NOT operation
# result_not = ~a
# print(result_not)

# #Bitwise left shift operation
# result_left_shift = a << 2
# print(result_left_shift)

# #Bitwise right shift operation
# result_right_shift = a >> 2
# print(result_right_shift)

#Example and Assignment
#Create a simple calculator function to calculate (add, subtract, multiply, divide)

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

def calculator():
    print('Conrad Simple Calculator')
    number1 = float(input("Enter the first number: "))
    number2 = float(input("Enter the second number: "))
    operator = input("Enter the operator (+,-,*,/):")

    if operator == '+':
        result = add(number1, number2)
    elif operator == '-':
        result = subtract(number1, number2)
    elif operator == '*':
        result = multiply(number1, number2)
    elif operator == '/':
        result = divide(number1, number2)
    else:
        print("Invalid operator")
        return
    print(f"The result is {result}")

if __name__ == '__calculator__':
    calculator()

#tkinter learn 
#Assignment create and simple calculator program with a GUI interface. 
# Make your title of the calculator program with program window with your name e.g "Jeff GEOF Simple calculator"
    
    













