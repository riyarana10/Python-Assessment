# Write a function that takes in a non empty array of integers that are sorted in ascending order and returns a new array 
# of same length with the square of original integers also sorted in ascending order.
# Sample input : [1,3,5,6]
# Sample output : [1,9,25,36]

intList = [1,3,5,6]
newlist = []
def sqaurefun(intlist):
    for i in intList:
        i = i**2
        newlist.append(i)
    return newlist



newlist = sqaurefun(intList)
print(newlist)



