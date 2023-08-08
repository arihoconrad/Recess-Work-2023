#Sets store multiple items in a single variable.
#unchangeable but one can remove and add items 

setone = {"Rice","Beans","Meat"}
print(setone)

#Duplicating is in sets

setone = {"Rice","Beans","Meat","Meat" }
print(setone)

#Exercise find the length of your set, data type, Acccessing items in a set, Add two sets together  

#Finding length of a set
print(len(setone)) #Outputs 3

#Finding data type of a set
print(type(setone)) #Outputs "set"

#Accessing items in a set(Checking for particular item in the set )
print("Meat" in setone)

#Adding two sets together

settwo = {"Apples","Chicken"}
print(setone.union(settwo))
