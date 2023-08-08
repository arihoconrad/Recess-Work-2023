#integers, floats, complex
a = 10 #int
b = 10.5 #float
c = 2j #complex

print(type(a))
print(type(b))
print(type(c))

#INTEGERS

x = 10
y = -10
z = 63275937

print(type(x))
print(type(y))
print(type(z))

#FLOATS

t = 10.5
h = -8.90
f = 63.275937

print(type(t))
print(type(h))
print(type(f))

#COMPLEX

g = 5 + 2j
j = -2j
i = 17 - 6j

print(type(g))
print(type(j))
print(type(i))

#Type conversions
e = 34 #int
f = 13.8 #float
g = 11j #complex

#Convert from float to complex
j = complex(f)
print(j)
print(type(j))

#Convert from int to complex
i = complex(e)
print(i)
print(type(i))

#Convert from complex to float
p = float(g.real)
print(p)
print(type(p))