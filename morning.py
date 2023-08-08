#LOOPS  
#Loops (for,while)

"""
for item in sequence:
"""
#Example of for loop
cars = ["Benz", "Jeep", "Volvo", "Ford","Toyota"]
for car in cars:
    print(car)

#Example on for loop using fruits
fruits = ["Apples", "Orange", "Watermelon", "Pineapples", "Grapes"]
for fruit in fruits:
    print(fruit)

#While loop
count = 0
while count < 5:
    print(count)
    count += 1

#Example of while loop
a = 0
while a < 5:
   print(a)
   a += 1

#Example2 of while loop
names = ["a", "b", "c", "d",] 
name_count = 0
while name_count < len(names):
    print(names[name_count])
    name_count += 1

#Break and continue statements
#Break statement

#Example of break statement
for number in range(1,10):
    if number == 5:
       break
    print(number)

#Continue statement
for number in range(1,10):
    if number % 2 == 0:
        continue
    print(number)

#Exception Handling 
"""
try:

except

finallly:
"""

#Example on exception handling
try:
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))
    c = a / b
    print(c)
except ZeroDivisionError:
    print("There is an error")
finally:
    print("Finally")

#Example5
#Dict is a dictionary {}

emotions = {
 "happy" : "I am happy",
    "sad" : "I am sad",
    "angry" : "I am angry"
}

# #convert to lowercase string

# #Prompt users to inpput their emotions
user_emotion = input("How are you feeling today?")

if user_emotion in emotions:
    print(emotions[user_emotion])

else:
    print("I don't understand how you feel")

#Exercise 
#Write program to ask students about their mental health
#Prompt students on a scale of 1 to 10 to rate their mental health

mental_health = {
    '1':"Very very bad",
    '2':"Very bad",
    '3':"Fairly very bad",
    '4':"Fairly bad",
    '5':"Fair",
    '6':"Fairly good",
    '7':"Fairly Very good",
    '8':"Very good",
    '9':"Fairly very good",
    '10':"Excellent!"
}

print("Greetings, please enter a number to check your mental health!!!")

number = input("Enter a number: ")
print(number)

if number in mental_health:
    print( mental_health[number])

else: 
    print("I dont know the state of your mental health. Please")