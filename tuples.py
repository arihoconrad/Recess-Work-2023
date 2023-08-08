#Tuples are used to store items in a single variable
#Tuples are ordered and unchangeable
 
phones = ("Samsung", "Iphone", "Tecno ")
print(phones)

#Tuples allow duplicate values 
  
phones = ("Samsung", "Iphone", "Tecno ", "Samsung", "Iphone", "Tecno ")
print(phones)

# Exercise use the len() with this tuple example  
phones = ("Samsung", "Iphone", "Tecno ", "Samsung", "Iphone", "Tecno ")
print(len(phones))

#Tuple showing different datatypes 

Tuple1 = ("Apple", "  Rice ")
Tuple2 = (1,2,3,4,5)
print(type(Tuple2))

#Exercise how to access tuples 
#Add items to turple
phones = ("Samsung","Iphone", "Tecno ")
z =list(phones)
z.append("Nokia") 
phones = tuple(z) 
print(phones)

#Adding two tuples together
Cars = ("Volvo", "Benz", "Spacio")
car = ("Subaru" ,)
Cars += car
Newstock = Cars + car

print(Cars)
print(car)
print(Newstock)