# Using dict comprehension create a dict having list items and their length as value.
# Example : {‘data’ : 4}

words = ['data', 'science', 'machine', 'learning']

myDict = {}

def add(myDict, key, value):
    myDict[key] = value

for i in words:
    add(myDict,i,len(i))


print(myDict)
    
