# #Inheritance
# class Animal:
#     def __init__(self, name):
#         self.name = name

#     def eat(self):
#         print(f"{self.name} is eating...")

# class Dog(Animal):
#     def bark(self):
#         print(f"{self.name} is barking...")

# class Cat(Animal):
#     def meow(self):
#         print(f"{self.name} is meowing...")

# #Create Animal objects
# animal = Animal("Generic Animal")
# dog = Dog("Spot")
# cat = Cat("Fluffy")

# #Invoke call eat method
# animal.eat()
# dog.eat()
# dog.bark()


# #Example2 Demostrating inheritance
# class Vehicle:
#     def __init__(self, brand, color):
#         self.brand = brand
#         self.color = color
    
#     def display_info(self):
#         print("Brand:", self.brand)
#         print("Color:", self.color)
    
#     def move(self,)

# class Car(Vehicle):

# #Exercise 1
# #Demostrate the use of inheritance to calculate area and perimeter of a circle and a rectangle
# #respectively (Shape: circle)    
# class Shape:
#     def __init__(self, radius):
#         self.radius = radius

# class Circle(Shape):
#     def __init__(self, radius):
#         super().__init__(radius)

#     def area(self):
#         return 3.14 * self.radius ** 2
    
#     def perimeter(self):
#         return 2 * 3.14 * self.radius

# class Rectangle(Shape):
#     def __init__(self, width, length):
#         super().__init__(width)
#         self.length = length

#     def area(self):
#         return self.width * self.length
    
#     def perimeter(self):
#         return 2 * (self.width + self.length)

# #Area and perimeter of Circle 
# my_circle = Circle(12)
# print("Area of circle: ", my_circle.area())
# print("Perimeter of circle: ", my_circle.perimeter())

# #Area and perimeter of Rectangle
# my_rectangle = Rectangle(10, 20)
# print("Area of rectangle: ", my_rectangle.area())
# print("Perimeter of rectangle: ", my_rectangle.perimeter())













# #Example 3
# #Multiple Inheritance
# class Animal:
#     def __init__(self, name):
#         self.name = name

#     def eat(self):
#         print(f"{self.name} is eating...")

# class Flyable:
#     def fly(self):
#         print(f"{self.name} is flying...")

# class Bird(Animal, Flyable):
#     def __init__(self, name, species):
#         super().__init__(name)
#         self.species = species

#     def display_info(self):
#         super().display_info()
#         print("Species:", self.species)
#         print("Name: {self.name}")

# # Create a Bird object
# my_bird = Bird("Pigeon","bird")

# # Invoke the bird methods
# my_bird.eat()
# my_bird.fly()

# #Method Overriding

# class Animal:
#     def make_sound(self):
#         print("Animal is making a sound")

# class Dog(Animal):
#     def make_sound(self):
#         print("Dog is making a sound")

# class Cat(Animal):
#     def make_sound(self):
#         print("Cat is making a sound")

# def make_animal_sound(animal):
#     animal.make_sound()

# # create objects
# animal = Animal()
# dog = Dog()
# cat = Cat()

# #Calling the make_animal_sound function
# make_animal_sound(animal)
# make_animal_sound(dog)
# make_animal_sound(cat)


#Polymorphism
#Polymorphism allows you to write code that can work with different objects
#Method overriding occurs when a derived class (child class), provides its own implementation of a method that is already defined in its subclass
#Method overloading allows a class to have multiple ethods withthe same name but different parameters


# #Example 4
# class Shape:
#     def calculate_area(self):
#         pass

# class Rectangle(Shape):
#     def __init__(self,length,width):
#         self.length = length
#         self.width = width

#     def calculate_area(self):
#         return self.length * self.width
    
# class Circle(Shape):
#     def __init__(self,radius):
#         self.radius = radius
#     def calculate_area(self):
#         return 3.14 * self.radius * self.radius
    
# # Create shaoe objects 
# rectangle = Rectangle(10,10)
# circle = Circle(10)

# # Calculate and display the area
# print("Area of Rectangle:", rectangle.calculate_area())
# print("Area of Circle:", circle.calculate_area())

# #Overloading functions


# #Abstraction 
# #Allows you to focus on essential features and hide them from unecessary details

# #Example 5: Demostration of abstraction
# from abc import ABC, abstractmethod

# class Vehicle(ABC):
#     # @abstractmethod
#     def start(self):
#         pass
#     # @abstractmethod
#     def stop(self):
#         pass

# class Truck(Vehicle):
#     def start(self):
#         print("Truck is starting...")
#     def stop(self):
#         print("Truck is stopping...")
    
# #Create Vehicle objects
# truck = Truck() 

# #Start the car
# truck.start()

# #Exercise2 Demostrate abstraction using calculating area of a circle and rectangle
# from abc import ABC, abstractmethod

# class Shape(ABC):
#     def __init__(self,name):
#         self.name = name
#     @abstractmethod
#     def area(self):
#         pass

# class Circle(Shape):
#     def __init__(self,name,radius):
#         super().__init__(name)
#         self.radius = radius
#     def area(self):
#         return 3.14 * self.radius * self.radius
    
# class Rectangle(Shape):
#     def __init__(self,name,length,width):
#         super().__init__(name)
#         self.length = length
#         self.width = width
#     def area(self):
#         return self.length * self.width

# #Create Shape objects
# circle = Circle("Circle",10)
# rectangle = Rectangle("Rectangle",10,10)

# #Calculate and display the area
# print("Area of Circle:", circle.area())
# print("Area of Rectangle:", rectangle.area())


#Assignment 1: Deadline 01 July 2023
#Create a receipt printing program with GUI interface, a mere advanced detail earns you more points
import tkinter as tk
from tkinter import messagebox

def print_receipt():
    # Get input values from the entry fields
    customer_name = customer_name_entry.get()
    item_name = item_name_entry.get()
    quantity = quantity_entry.get()
    price = price_entry.get()

    # Validate the input fields
    if customer_name == "":
        messagebox.showerror("Error", "Please enter customer name.")
        return

    if item_name == "":
        messagebox.showerror("Error", "Please enter item name.")
        return

    if quantity == "" or not quantity.isdigit():
        messagebox.showerror("Error", "Please enter a valid quantity.")
        return

    if price == "" or not price.replace(".", "").isdigit():
        messagebox.showerror("Error", "Please enter a valid price.")
        return

    # Calculate the total cost
    total_cost = float(quantity) * float(price)

    # Create the receipt message
    receipt_message = f"Customer Name: {customer_name}\n"
    receipt_message += f"Item: {item_name}\n"
    receipt_message += f"Quantity: {quantity}\n"
    receipt_message += f"Price: {price}\n"
    receipt_message += f"Total Cost: {total_cost}\n"

    # Display the receipt message in a message box
    messagebox.showinfo("Receipt", receipt_message)

# Create the main window
window = tk.Tk()
window.title("Receipt Printing Program")

# Create labels and entry fields for input
customer_name_label = tk.Label(window, text="Customer Name:")
customer_name_label.pack()
customer_name_entry = tk.Entry(window)
customer_name_entry.pack()

item_name_label = tk.Label(window, text="Item Name:")
item_name_label.pack()
item_name_entry = tk.Entry(window)
item_name_entry.pack()

quantity_label = tk.Label(window, text="Quantity:")
quantity_label.pack()
quantity_entry = tk.Entry(window)
quantity_entry.pack()

price_label = tk.Label(window, text="Price:")
price_label.pack()
price_entry = tk.Entry(window)
price_entry.pack()

# Create the Print Receipt button
print_button = tk.Button(window, text="Print Receipt", command=print_receipt)
print_button.pack()

# Start the Tkinter event loop
window.mainloop()

#In this program we do not at units to our quantity and cuurency to our price





