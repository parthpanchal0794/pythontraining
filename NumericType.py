"""
Numeric types classes
    1. Integer e.g 10
    2. Float e.g 10.0
    3. Complex e.g 3 + 5j
    4. Binary type (Class Int)
    5. Hexadecimal (Class Int)
    6. Octa decimal (Class Int)
"""

# Integer Values
a = 13
b = 100
c = -66
print(a, b, c)
print(type(a))

# Floating values
x = 33.44
y = -8.78
z = 56.0  # with .0 at end it will consider as integer but with .0 it will consider as float
print(x, y, z)
print(type(z))

# Complex type
d = 3 + 5j
print(d)
print(type(d))

# Binary type
# To define binary type start with literal 0b or 0B
e = 0b1010
g = 0B1010
print(e)
print(g)
print(type(e))

# Hexadecimal type
# To define hexadecimal start with literal 0x or 0X
f = 0XFF
h = 0xFF
print(f)
print(h)
print(type(f))

# Octa decimal type
# To define octa decimal start with literal 0o or 0O
i = 0o12
j = 0O12
print(i)
print(j)
print(type(i))

#################################################################

# Boolean value type have 2 value: True and False
# it mainly use to define condition in loop or if statement

k = True
print(type(k))
print(9 > 8)  # Condition returns True value of class bool

###################################################################

# int, float, bin, hex and oct functions used to convert the numeric data type class

A = int(55.60)  # float or int no are allowed
print(type(A))

C = float(66)
print(type(C))
D = float("66")  # only no are allowed not string like "python"
print(type(D))

E = bin(10)  # only integers are allowed
print(type(E))
print(E)

F = hex(10)  # only integers are allowed
print(type(F))
print(F)

G = oct(10)  # only integers are allowed
print(type(G))
print(G)
