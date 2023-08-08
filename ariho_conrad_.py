#Dictionaries are alos datatyped used to store datanvalues in key:value pairs
#Dictionaries are ordered, changeable but do not allow dupicates 

mydict = {
    "Phone": "Iphone",
    "Iphonemodel": "Iphone15",
    "year": 2023
}
print(mydict)

#Length of dictionary
print(len(mydict))

#Data type
print(type(mydict))

#Accessing Dictionary items
z = mydict["year"]
print(z)

#Accessing dictionary items using getter and setter methods
z = mydict.get("Phone")
print(z)

#Accesiing dictionary keys
w = mydict.keys()
print(w)

#Exercise 1: use the values() method to return a list of all the dictionary
dict = mydict.values()
print(dict)

#Exercise 2: to check if a key does exist in the dictionary
if "Iphonemodel" in mydict:
    print("Yes")
else:
    print("No")
#Exercise 3: Give an example on how to change dictionary items, how to update 
mydict["Iphonemodel"] = "Iphone16"
print(mydict)
mydict.update({"Iphonemodel": "Iphone17"})
print(mydict)

#Exercise 4: use the items() method to return a list of all the dictionary
dict = mydict.items()
print(dict)

#Exercise 4: Give and example on how to add dictionary items, how to remove dictionary items
mydict.update({"Iphonemodel": "Iphone18"})
print(mydict)
mydict.pop("Iphonemodel")
print(mydict)

#Exercise 5: use the clear() method to remove all the items from the dictionary
mydict.clear()
print(mydict)

#Exercise 5: Give an example on how to loop through a dictionary and aslo how to nest dictionaries
#Looping through both keys and values in the dictionary
mydict = {
    "Phone": "Iphone",
    "Iphonemodel": "Iphone15",
    "year": 2023
}
for x,y in mydict.items():
    print(x,y)

# #Nested dictionaries
mydict = {
    "Phone": "Iphone",
    "Iphonemodel": "Iphone15",
    "year": 2023
}
for x,y in mydict.items():
    print(x,y)
    if x == "Iphonemodel":
        mydict[x] = "Iphone16"
        print(mydict)
    else:
        mydict[x] = "Iphone17"
        print(mydict)

#Exercise 6: use the copy() method to create a copy of the dictionary
mydict = {
    "Phone": "Iphone",
    "Iphonemodel": "Iphone15",
    "year": 2023
}
mycopy = mydict.copy()
print(mycopy)

#STRINGS
#Exercise 1: use the len() function to determine the length of a string
mystring = "I love Python Programming"
print(len(mystring))

#Exercise 2: give an example of using a for loop in a string
mystring = "I love Python Programming"
for x in mystring:
    print(x)

#Exercise 3: Give an example of slicing in strings
mystring = "I love Python Programming"
print(mystring[0:5])
print(mystring[5:])
print(mystring[:5])
print(mystring[:])

#Boolean values
#Exercise use a condition to show how to use booleans
mystring = "I love Python Programming"
if "Hello" in mystring:
    print("Yes")
else:
    print("No")

