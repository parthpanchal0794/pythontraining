l = []  # to define a empty list

# list type can contain multiple data type like int, str, float
lst = ["Parth", 12, 10.56, -3]
print(lst)

# We can use slicing, indexing and repetition
print(lst[1])  # returns 1st index --> 12
print(lst[1:3])  # returns 1st and 2nd index just like slicing on string --> 12. 10.56
print(lst * 4)  # returns list with multiplication by the value provided. in this case its 4 times
print(len(lst))  # return len of the list

# To add a value in a list
lst.append(40)  # adds 40 at a last index of a list
print(lst)

# To remove a value in a list
lst.remove(12)  # Remove the last index with provided value
print(lst)

# To remove the value by index
del (lst[1])
print(lst)

lst.append(30)
lst.append(30.05)
lst.remove("Parth")
print(lst)

# Max fn to get the max value of a list. Throw error if any value have str type as max works with int or float data type
print(max(lst))

# Min fn to get the min value of a list.
print(min(lst))

# Insert fn to add a value at given index. It shift the existing value of a given index by 1
lst.insert(1, 45)  # in this case 45 will be assigned at index 1 and 40 will be now shift to index 2
print(lst)

# Sort fn to sort the list in desired way. By default ascending order
lst.sort()
print(lst)

# if we want in descending order
lst.sort(reverse=True)
print(lst)

# clear fn to remove all the items on a list
lst.clear()
print(lst)

##############################################################################################################

"""
Tuple is a another list type. the difference between tuple and a list type is, list can be modified but
tuple can't be modified.
We can not use functions like append(), extend(), insert(), remove(), clear() on tuple
"""

# To define a empty tuple by "()" bracket
tpl = ()

t = (40, 50, 45.67, "XYZ")

# if we need to define only one element in a tuple then before closing bracket you need to add a comma else it will
# consider as variable holding one value
t1 = (40,)
print(type(t1))

# we can perform indexing and repetition on tuple. Slicing is not allowed on tuple class
print(t[1])
print(t*2)

# count fn to get a no of times any value occurred in tuple
print(t.count(50))

# Index fn to get a index of a value
print(t.index(50))

# tuple fn to convert list to tuple
# if we assign same variable it will convert it to tuple form
l2 = [10, 20, 30]
print(type(l2))
t2 = tuple(l2)
print(type(t2))
print(l2)
print(t2)
