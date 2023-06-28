# Write a function that takes in a non empty array of distinct integers and an integer representing a target sum. 
# If any two numbers in the input array sum up to the target sum, the function should return them in an array, in any order. 
# If no two numbers sum up to target sum, the function should return an empty array. 
# Note that the target sum has to be obtained by summing two diff integers in the array; you can’t add a single integer 
# to itself in order to obtain the target sum.
# You can assume that there will be at most one pair of numbers summing up to the target sum.
# Array = [3, 5, -4, 8, 11, 1, -1, 6]
# Targetsum = 10
# Sample output
# [-1,11]


arr = [3, 5, -4, 8, 11, 1, -1, 6]
sum = 8

res = []
def pairsum(arr,sum,res):
    n = len(arr)
    for i in range(n):
        currSum = 0
        for j in range(i+1,n):
            currSum = arr[j]+arr[i]
            if(currSum == sum):
                res.append(arr[i])
                res.append(arr[j])   
        
    return res

result = pairsum(arr,sum,res)
print(result)                                   
