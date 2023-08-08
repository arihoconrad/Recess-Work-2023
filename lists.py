#Lists are used to store many items in one single variable
#Lists are ordwered, changeable and allow duplicate values 
#Afternoon = ['conrad','trevor','steven']
#print(Afternoon)

#Duplicates in Lists
#Lists are mutable
Afternoon = ['conrad','trevor','steven','Trisha','Martha']
print(Afternoon)

#List length
print(len(Afternoon))
#Type
print(type(Afternoon))

#Accessing List Items
#Lists use index notation much like Arrays
print(Afternoon[0])
print(Afternoon[1])
print(Afternoon[2])
print(Afternoon[3])
print(Afternoon[4])
#Accessing all items of the list

print(Afternoon[-3])

print(Afternoon[-5] + " is always with " + Afternoon[-2])

#Accesssing a range of items
print(Afternoon[0:3])
print(Afternoon[1:4])
print(Afternoon[:2])
print(Afternoon[2:])
print(Afternoon[:])

#Inserting items into a list 
Afternoon.append('Drake')
print(Afternoon)

#Inserting and item using the index method
Afternoon.insert(0,'Drake')
print(Afternoon)

#Removing items from a list
Afternoon.remove('Drake')
print(Afternoon)

Afternoon.pop()
print(Afternoon)