import os 
#Exception Handling
#Exception handling helps to prevent your program from abruptly terminating whenerrors occu
"""
In Python, there are several built-in exceptions that can be raised when an error occurs during the execution of a program. Here are some of the most common types of exceptions in Python:

SyntaxError: This exception is raised when the interpreter encounters a syntax error in the code, such as a misspelled keyword, a missing colon, or an unbalanced parenthesis.

TypeError: This exception is raised when an operation or function is applied to an object of the wrong type, such as adding a string to an integer.

NameError: This exception is raised when a variable or function name is not found in the current scope.

IndexError: This exception is raised when an index is out of range for a list, tuple, or other sequence types.

KeyError: This exception is raised when a key is not found in a dictionary.

ValueError: This exception is raised when a function or method is called with an invalid argument or input, such as trying to convert a string to an integer when the string does not represent a valid integer.

AttributeError: This exception is raised when an attribute or method is not found on an object, such as trying to access a non-existent attribute of a class instance.

IOError: This exception is raised when an I/O operation, such as reading or writing a file, fails due to an input/output error.

ZeroDivisionError: This exception is raised when an attempt is made to divide a number by zero.

ImportError: This exception is raised when an import statement fails to find or load a module.
"""

#Below are some examples of exceptions
#ZeroDivisionError
try:
    numerator = 10
    denominator = 0

    result = numerator/denominator

    print(result)
except:
    print("Error: Denominator cannot be 0.")

# Output: Error: Denominator cannot be 0. 

# Type error
x = 5
y = "hello"
try:
	z = x + y
except TypeError:
	print("Error: cannot add an int and a str")

# Output: Error: cannot add an int and a str

#Example with the finally block
#The finally block runs whether there is an exception or not and it can be optional 
try:
    numerator = 10
    denominator = 0

    result = numerator/denominator

    print(result)
except:
    print("Error: Denominator cannot be 0.")
    
finally:
    print("This is finally block.") #Always executes

#Index Error
try:
    my_list = [1, 2, 3]
    print(my_list[4])
except IndexError:
    print("Error: Index out of range.")

# Output: Error: Index out of range.


#Examples of Value Error,Zero Divion Error,and Exception class that catches other errorrs
def division():
    try:
        dividend = int(input("Enter the dividend: "))
        divisor = int(input("Enter the divisor: "))

        result = dividend / divisor
        print("Result:", result)

    except ValueError:
        print("Invalid input. Please enter integers only.")

    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")

    except Exception as e:
        print("An error occurred:", e)

division()


#Attribute Error

# Python program to demonstrate
# AttributeError


class Geeks():
	
	def __init__(self):
		self.a = 'GeeksforGeeks'

# Driver's code
obj = Geeks()

# Try and except statement for
# Exception handling
try:
	print(obj.a)
	
	# Raises an AttributeError
	print(obj.b)
	
# Prints the below statement
# whenever an AttributeError is
# raised
except AttributeError:
	print("There is no such attribute")



#File Handling
"""
File handling in Python takes place in the following order:
1. Open a file
2. Read or write(perform operation)
3.Close the file

Advantages of file handling
1.Versatility
2. Flexibility
3. User friendly
4. Cross-platform support

Disadvantages of file handling
1. Erro prone
2. Security risks
3. Complexity
4. Performance 

Where the following mode is supported:

r: open an existing file for a read operation.

w: open an existing file for a write operation. If the file already contains some data then it will be overridden but if the file is not present then it creates the file as well.

a:  open an existing file for append operation. It won’t override existing data.

 r+:  To read and write data into the file. The previous data in the file will be overridden.

w+: To write and read data. It will override existing data.

a+: To append and read data from the file. It won’t override existing data.


"""
# #Example that includes reading and writing data from a file
# # a file named "geeks", will be opened with the reading mode.
# file = open('geeks.txt', 'w')
# file.write('My name is Ariho Conrad\n' )
# file.write('I am 21 years old\n' )
# file.write("i love python programming\n")

# file = open('geeks.txt', 'r')


# # This will print every line one by one in the file
# for each in file:
# 	print (each)
        

# file.close()

# #To append a file
# file = open('geeks.txt', 'a')
# file.write('I am a geek')
# file.close()

# # #To delete a file
# # os.remove('geeks.txt')

# Writing to a file
def write_to_file(file_name, content):
    try:
        with open(file_name, 'w') as file:
            file.write(content)
        print("Content written to the file successfully.")
    except IOError:
        print("An error occurred while writing to the file.")

# Reading from a file
def read_from_file(file_name):
    try:
        with open(file_name, 'r') as file:
            content = file.read()
        print("File content:")
        print(content)
    except IOError:
        print("An error occurred while reading the file.")

# Test the functions
file_name = "example.txt"
content = "Hello, world!"

write_to_file(file_name, content)
read_from_file(file_name)



#A simple python program to demostrate file operations
#Creating the file
def create_file(filename):
    try:
        with open(filename, 'w') as file:
            print("File created:", filename)
    except IOError:
        print("Error: Unable to create the file.")
#Writing to the file
def write_to_file(filename, content):
    try:
        with open(filename, 'w') as file:
            file.write(content)
        print("Data written to the file successfully.")
    except IOError:
        print("Error: Unable to write to the file.")
#Appending to the file
def append_to_file(filename, content):
    try:
        with open(filename, 'a') as file:
            file.write(content)
        print("Data appended to the file successfully.")
    except IOError:
        print("Error: Unable to append to the file.")
#Reading from the file
def read_file(filename):
    try:
        with open(filename, 'r') as file:
            data = file.read()
            print("Data read from the file:\n", data)
    except FileNotFoundError:
        print("Error: File not found.")
    except IOError:
        print("Error: Unable to read from the file.")
#Deleting the file
def delete_file(filename):
    import os
    try:
        os.remove(filename)
        print("File deleted successfully:", filename)
    except FileNotFoundError:
        print("Error: File not found.")
    except PermissionError:
        print("Error: Permission denied.")

if __name__ == "__main__":
    filename = "example.txt"
    create_file(filename)

    content = "Hello, this is a sample content.\n"
    write_to_file(filename, content)

    append_content = "This content is appended.\n"
    append_to_file(filename, append_content)

    read_file(filename)

    delete_file(filename)



