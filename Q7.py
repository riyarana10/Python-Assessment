# Remove all the vowels from a string using list comprehension. 

s = "helloworld"
# s.lower()
newList = [i for i in s if i not in "aeiouAEIOU"]

print(newList)