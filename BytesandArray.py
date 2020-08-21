# Max value we can provide to be a byte is 255

lst = [10, 30, 50, 234]
print(type(lst))

# bytes fn used to convert integer data types to bytes
b = bytes(lst)
print(type(b))
print(b)
# we can not perform index assignment on bytes
# e.g b[1] = 33 throws a error

# bytearray convert integer data type to bytearray
b1 = bytearray(lst)
print(type(b1))

# We can add or modify a object in bytearray but slicing or repetition is not allowed in bytearray or bytes.
print(b1)
b1[2] = 60
print(b1)