#Object Oriented Programming
#Key concepts are 
# 1.Class 
# 2.Object 
# 3.Encapsulation 
# 4. Inheritance
# 5. Abstraction
#Classes and Objects 
"""

"""
#  
#Encapsulation
#Key main goal of encapsulation are 
"""
1. To hide the implementation details of a class.
2. To protect the integrity of a class.
3. To protect the integrity of an object.
"""
# Exercise 1: claculate the area and circumference of a circle

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius
    
    def circumference(self):
        return 2 * 3.14 * self.radius
    
my_circle = Circle(radius=13)
print(my_circle.area())
print(my_circle.circumference())

#Encapsulation is a mechanism to hide the implementation details of a class.

#Example with a bank account

# class BankAccount:
#     def __init__(self, account_number, balance):
#         # Encapsulates the account number attribute
#         self.__account_number = account_number
#         # Encapsulates the balance attribute
#         self.__balance = balance

#     def deposit(self, amount):
#         self.__balance += amount # Encapsulates the deposit

#     def withdraw(self, amount):
#         if self.__balance >= amount:
#             self.__balance -= amount # Encapsulates the withdraw
#         else:
#                     print("Insufficient funds")

#     def get_balance(self):
#          return self.__balance
    
# #Create a Bank Object
# my_account = BankAccount("123456789", 1000)

# #Access the Bank Object and modify encapsulated attributes indirectly
# print(my_account.get_balance())
# my_account.deposit(500)
# print(my_account.get_balance())
# my_account.withdraw(100)
# print(my_account.get_balance())



#Exercise 2: Convert temperature(37) from Celcius to Fahrenheit

# class TemperatureConverter:
#     def __init__(self, temperature):
#         self._temperature = temperature

#     def get_temperature(self):
#         return self._temperature

#     def set_temperature(self, temperature):
#         self._temperature = temperature

#     def celsius_to_fahrenheit(self):
#         return (self._temperature * 9/5) + 32


# # Create an instance of TemperatureConverter
# converter = TemperatureConverter(37)

# # Get the current temperature in Celsius
# print("Temperature in Celsius:", converter.get_temperature())

# # Convert Celsius to Fahrenheit
# fahrenheit_temp = converter.celsius_to_fahrenheit()
# print("Temperature in Fahrenheit:", fahrenheit_temp)

# # Update the temperature
# converter.set_temperature(25)

# # Convert the updated temperature to Fahrenheit
# updated_fahrenheit_temp = converter.celsius_to_fahrenheit()
# print("Updated temperature in Fahrenheit:", updated_fahrenheit_temp)

#Assignment 1. Show encapsulation with employee information to give a pay incrementation
#Salary with employee information to new_salary e.g 850000 to 100000


#Defining our class Employee 
class Employee:
    def __init__(self, name, salary):
        self._name = name
        self._salary = salary
        
    def new_salary(self):
        new_salary = self._salary + (self._salary * 0.1)
        return new_salary
    
    def display_details(self):
        print("Name: ", self._name)
        print("Salary: ", self._salary)
        print("New Salary: ", self.new_salary())

#creating an object of Employee 
my_employee = Employee("Conrad", 850000)
my_employee.new_salary()
my_employee.display_details()