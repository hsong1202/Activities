fruit = 'banana'
# letter = fruit[1]
# print(letter)

# for letter in fruit:
#     print(letter)

fruitlength = len(fruit)
print(fruitlength)

# i = 0
# while i < fruitlength:
#     print(f"this is fruit letter:{fruit[i]}")
#     print(f"this is iteration number{i}")
#     i = i + 1

# print(dir(type(fruit)))

# print(help(str.count))

data = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'

atpos = data.find('@')

print(atpos)

sppos = data.find(' ',atpos)

print(sppos)

host = data[atpos+1:sppos]

print(host)

# Exercise 5: Take the following Python code that stores a string: str = 'X-DSPAM-Confidence:0.8475'

# Use find and string slicing to extract the portion of the string after the colon character and then use the float function to convert the extracted string into a floating point number.

# Exercise 6: Read the documentation of the string methods at https://docs.python.org/library/stdtypes.html#string-methods You might want to experiment with some of them to make sure you understand how they work. strip and replace are particularly useful.

# The documentation uses a syntax that might be confusing. For example, in find(sub[, start[, end]]), the brackets indicate optional arguments. So sub is required, but start is optional, and if you include start, then end is optional.

# str = 'X-DSPAM-Confidence:0.8475'