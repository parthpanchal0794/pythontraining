s = "You are awesome"
print(s)
s1 = """You are
a creator
of your destiny"""
print(s1)

# Indexing is a concept of reaching out perticular char from string. it also work with list, tuple as well
# Index start with 0 and it goes till len -1
print(s[1]) # --> o
print(s[0])

# Repetition is a operator which multiplies the string
print(s*2) # --> You are awesomeYou are awesome

# len is a inbult function returns the no of item in a container
print(len(s)) # --> 15

"""
Slicing is a concept of getting some value of string by providing starting and ending index of a string
Slicing does not include the element at a end.
Slicing does not include last index

# Syntax [starting index: ending index: step value(optional)]

no of element = higher index - lower index
    for ex: a = PARTH
            a[1:4] returns "ART" and no of element 4-1 = 3
    
Indexing example for slicing

Positive Index          Negative Index
        0           P           -5
        1           A           -4
        2           R           -3
        3           T           -2
        4           H           -1

Step value is no of place python jumps to go from one index to another
Default value of step is 1
we can pass step parameter in 3rd colon
    for ex a[1:5:2] retuns "AT" as it jumps 2 step at a time
we can also provide -1 as a step value to go to reverse order
    for ex a[3:1:-1] returns "TR" as it jumps in reverse
"""
a = "PARTH"
print(a[0:5]) # --> "PARTH" as 5th element is not included
print(a[0:]) # --> returns the all element starting with 0th index "PARTH"
print(a[1:4]) # --> returns the starting with 1st index to 4th index "ART"
print(a[3:]) # --> returns the all element starting with 3rd index "TH"
print(a[:4]) # --> returns the all element starting with 0th index till 4th index "PART"
print(a[-3:]) # --> return the all element starting with -3 to last index "RTH"
print(a[1:4:2]) # return "AT" as it return all element starting with 1st index to 4th index but jump 2 step at a time
print(a[3:1:-1]) # return "TR" as it return element starting with 3rd index to 1st index in reverse order
print(a[1:4:-1]) # return blank line as no correct order
print(a[::-1]) # return the string in reverse order "HTRAP"

# Strip fn used to remove all the white spaces at a begining and ending of the string

b = "  You are great  "
print(b)
print(b.strip())

# lstrip fn return the copy of the string with all the white space from left side removed
print(b.lstrip())
print(b)

# rstrip fn return the copy of the string with all the white space from right side removed
print(b.rstrip())
print(b)

# find fn to find the starting index of a given substring
f = "You are awesome"
print(f.find("are")) # --> returns 4 as "are" starts with 4th index
print(f.find("are",5,len(f))) # we can also pass start and end index between which we need to find substring
# find fn return -1 if value not found

# count fn gives no of occurences found for given substring for a string
print(f.count("a")) # --> returns 2 as there are 2 a's in a string

# replace fn replace the old substring with new substring. it doesn't change old string but makes a copy of it.
print(f.replace("awesome","super"))
print(f)

print(f.upper()) # Convert to upper case
print(f.lower()) # Convert to lower case
print(f.title()) # Convert to title case

########## Assignment ################

i = 10
f = 20.54
b = True # remember to type first letter as capital to define bool type variable
s = "I am the best"

print(i)
print(f)
print(b)
print(s)

