a = "ali akbar"
a.upper() # does not change the original string
print(a.upper()) # ALI


print(a.replace("ali", "reza")) # does not change the original list

a=a.replace("ali", "haider") # changes the original string
print(a) # ali akbar

print(sorted(a)) # returns a new sorted list of characters in the string

a = list(a)
print(a.sort()) # gives None because sort() method sorts the list in place and returns None
print(a)

e_id= "US-2-15-8765432"

print(e_id.split("-")) # returns a list of strings split by the delimiter "-"

