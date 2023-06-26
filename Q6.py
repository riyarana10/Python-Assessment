# Count the number of spaces in a string using list comprehension. Eg string : “my name is Khan”.

s = "my name is khan"
spaceCountList = [i for i in s if i == ' ']

print(spaceCountList)
print("space count for the string s is : ",len(spaceCountList))