# Set type like list type, can store various type of data type like int, str, float etc..
# Set removes duplicates if found

s = {}  # Define empty set/Dict

s1 = {10, 20.10, -4, "parth", 10}  # Set assignment
print(s1)
print(type(s1))

# Update fn used to add value in a set
s1.update([99, 33])
print(s1)
s1.update([90, 35])  # it will update value at any random index
print(s1)

# As set not carry any order in saving the objects we can't perform indexing, slicing or repetition on sets

# Remove fn to remove object from set
s1.remove(33)  # it only take one argument. we can't add multiple objects to remove like update fn
print(s1)

# Frozenset fn make a copy of set to a frozen set
f = frozenset(s1)
print(type(f))
print(type(s1))

# We can not perform update or remove operation on frozen set
