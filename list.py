# EXERCISE 1 : Lists
# 1
people = ["peter", "samuel", "opolot", "mike", "ariho"]
print(people[1])


# 2
people[0]= "erica"
print (people[0])

# 3
people.append("jeremy")
print(people)

# 4
print(people[-1])

# 5
people.pop(3)
print(people)

# 6
print(people[-1])

# 7
people= ["hana", "conrad", "saul", "ian", "calvin", "kevin", "Lex"]
print(people[2:4])

# 8
country = ["china", "Russia","UK", "Belgium"]
countries_copy = country.copy()
print(countries_copy)

# 9 
for countries in country:
    print("countries")

# 10 
animals = ["dog", "cat", "pig", "hen"]
# ascending order
animals.sort()
print(animals)
# descending order
animals.sort(reverse=1)
print(animals)

# 11
for animal in animals:
    if "a" in animal:
        print(animal)

# 12 s
first_names = ["jenny", "trisha", "esther","martha" ]
second_names = ["akram", "ariho", "apio", "smith"]
print(first_names + second_names)

# EXERCISE TWO
# 1
phones = ("samsung", "iphone", "techno", "redmi")
print("My favourite brand is" ,phones[1])

# 2
print(phones[-3])

# 3
phoneslist = list(phones)

phoneslist[1] = "itel"
phonestuple = tuple(phoneslist)
print(phonestuple)

# 4
addphones = list(phones)
addphones.append("Huawei")
x= tuple(addphones)
print(x)

# 5
for phone in phones:
    print(phone)

# 6
deletinglist = list(phones)
deletinglist.pop(0)
newphones = tuple(deletinglist)
print(newphones)

# 7
tuples = tuple(["Kampala", "Jinja", "Mbra", "Mbale"])
print(tuples)

# 8
names = ("Conrad", "Collins")
first_name, last_name = names
print(first_name)
print(last_name)

# 9
tuple3 = tuple(["Kampala", "Jinja", "Mbra", "Mbale"])
print(tuple3[1:])

# 10
first_name = "Conrad"
sec_name = "Ariho"
full_name = first_name + sec_name
print(full_name)

# 11
colors = ("red", "white","blue")
multiplied = colors*3
print(multiplied)

# 12
thistuple = (1,3,7,8,7,5,4,6,8,5)
numberoftimes = thistuple.count(8)
print(numberoftimes)

# EXERCISE THREE
# 1
beverages = set(("nile", "water", "bell"))
print(beverages)

# 2
beverages.add("tusker")
beverages.add("juice")
print(beverages)

# 3
mySet = {"oven","kettle","microwave","refrigerator"}
print("microwave" in mySet)

# 4
mySet.remove("kettle")
print(mySet)

# 5
for item in mySet:
    print(item)

# 6
mySet = {"oven","kettle","microwave","refrigerator"}
mySecSet = {"fridge","pot"}
x= set(mySecSet)
print(mySet.union(x))

# 7
ages= {45,67,43}
first_name= {"Conrad", "Emma", "Michael"}
joint_set = ages.union(first_name)
print(joint_set)

#Excercise4(Strings)
#1
a = 12
b = "Ariho"
concatenated = str(a) + b
print(concatenated)

#2
txt = "Hello, Uganda!"
stripped = txt.strip()
print("Stripped string: " , stripped)

#3
uppercase_txt = txt.upper()
print("Capitalized string: " , uppercase_txt)

#4
replaced_txt= txt.replace("U", "V")
print("Replaced string: " , replaced_txt)

#5
y = "I am proudly Ugandan"
range_of_chars = y[1:4]
print("Range of characters: ", range_of_chars)

#6
x = 'All "Data Scientists" are cool!'
print("Corrected string: ", x)

# Exercise5(Dictionaries)
#1
Shoes = {
    "brand": "Nick",
    "color": "black",
    "size": "40"
}

#2
Shoes.update({"brand": "Adidas"})
print(Shoes)

#3
Shoes["type"] = "sneakers"
print(Shoes)

#4
print(Shoes.key())

#5
print(Shoes.values())

#6
if "sizes" in Shoes.keys():
    print("yes")
else:
    print("no")

#7
for i in Shoes:
    print(Shoes[i])

#8
Shoes.pop("color")
print(Shoes)

#9
Shoes.clear()
print(Shoes)

#10
names = {
    "peter": "23",
    "samuel": "34",
    "opolot": "19",
    "mike": "26",
    "ariho": "21"
}
names_copy = names.copy()
print(names)
print(names_copy)

#11
school = {
    "headteacher" : {
        
        "name" : "Deodat",
        "role": "administration"
    },
    "teacher" : {
        "name" : "Ituuma",
        "role": "teaching"
    },
    "student" : {
        "name" : "Ariho",
        "role": "studying"
    }
}
print(school["teacher"]["name"])

#Loopoing through nested dictionary
for i in school:
    for j in school[i]:
        print(school[i][j])