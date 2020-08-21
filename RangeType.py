# range fn to set a range
r = range(5)  # It will create a range starting with 0 to 4 (n-1)

for i in r:
    print(i)

# We can provide start index value as well to start a range from a desired value
r1 = range(1, 6)  # Create a range from 1 to 5.
for i in r1:
    print(i)

# We we need to jump specific value between starting index and end index, we can also provide step value.
r2 = range(1,15,3) # Create a range (1,4,7,10,13) Jumping 3 at a step
for i in r2:
    print(i)
