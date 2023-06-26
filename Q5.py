# Find all of the numbers from 1–1000 that are divisible by 8 using list comprehension.

numlist = [i for i in range(1,1000) if i%8 == 0]

print(numlist)

