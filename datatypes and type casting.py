# Data types in python
# To print a specific character in a string, we use index number.
# The index numbers starts with 0.(Subscript)
print("Salient Patient"[6])
# Integer datatype
print(564+765)
# We can find the type of input data by type check function.
name = input("What is your name? ")
print(type(name))
# Type Casting
# we can also change the type of input data.
name_char = len(name)
print(type(name_char))
# Changing the int datatype into string datatype
name_char_str = str(name_char)
print("Your name has " + name_char_str + " characters")
# we can also convert directly
print( 65 + float(109) )


