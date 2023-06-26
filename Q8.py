# “A Python list comprehension consists of brackets containing the expression, which is executed for each element along with the for loop 
# to iterate over each element in the”
# Find all the words in the string having length less than 4 letters using list comprehension.

s = "He turned Random back and headed for the camp"
words = s.split()
print(words)
mylist = [word for word in words if len(word)<4]
print(mylist)
