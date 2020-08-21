"""
Dictionary type assignment sample: {Key:Value}
For EX: b = {1:"Parth"}
We can use any object as a key and any object as a value
"""
d1 = {1: "PARTH", 5: 8.9, "SID": 4}
print(d1)

# item fn to get both keys and values of a dictionary
print(d1.items())

# keys fn to get all the keys in a dictionary with set like object
print(d1.keys())

# values fn to get all the keys in a dictionary with set like object
print(d1.values())

# We can loop through keys or values
k = d1.keys()
for i in k:
    print(i)

v = d1.values()
for i in v:
    print(i)

print(d1[1])  # to access value of a key. Here 1 is not a index but a key defined in a dictionary

# del fn to delete a element in  a dictionary
print(d1)
del d1[1]  # Here also 1 is a key defined in a dictionary
print(d1)
