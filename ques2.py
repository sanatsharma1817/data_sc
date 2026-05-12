# Q. write a program which contains different functions, the 1st
# function converts list which was given by the user into a matrix format of 3*3,
# 2nd function will convert the same list into a tuple and find the
# mean, median and the mode and the 3rd function will iterate over this
# two functions and find the gaps fill with null values respectively and gives a
# dictionary format mapped with first to the second function.
import statistics
nums = []
print("enter 9 numbers")
for i in range(9):
    n = int(input())
    nums.append(n)
print("matrix is :")
k = 0
for i in range(3):
    for j in range(3):
        print(nums[k], end=" ")
        k += 1
    print()
t = tuple(nums)
print("tuple is :", t)
print("mean is :", statistics.mean(t))
print("median is :", statistics.median(t))
print("mode is :", statistics.mode(t)) 
d = {}
for i in range(len(nums)):
    d[nums[i]] = t[i]
print("dictionary is :")
print(d)