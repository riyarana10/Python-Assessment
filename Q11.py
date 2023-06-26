# You are given a list of integers and an integer. Write a function that moves all instances of that integer in the list to 
# the end of the list and returns the list.
# Sample input : [2,1,2,2,2,3,4,5]
# toMove = 2
# Sample output : [1,3,4,5,2,2,2,2]


# 1st method using inbuilt fucntions

inputList = [2,1,2,2,2,3,4,5]
# givenInt = input("enter number")
integer = 2
# occ = inputList.count(integer)
# print(occ)
def sortList(mylist,integer):
    occ = mylist.count(integer)
    mylist = [i for i in mylist if i!=integer]
    mylist.extend([integer]*occ)
    
    return mylist

result = sortList(inputList,integer)
print(result)





