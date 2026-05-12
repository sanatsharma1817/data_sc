# Write a program using functions to add two numbers. If the sum of these two numbers
# is greater than the middle value of a user-provided list, print the set of all 
# numbers in the list located between the start and the middle value. 
# If the sum is equal to the middle value, print a dictionary where the key
# is the index of the middle value and the value is the middle value itself. 
# If the sum is less than the middle value, print a tuple containing all numbers 
# in the list that appear after the middle value.[1, 2] solve this ques in python 
# for begineer

numm = [1, 2, 3, 4, 5] 
a = int(input("enter first number : "))
b = int(input("enter second number : ")) 
total = a + b 
print("sum is :", total) 
mid_indx = len(numm) // 2 
mid_val = numm[mid_indx]
print("middle value is :", mid_val) 
if total > mid_val:
    print("sum is greater than middle val")
    ans = set(numm[:mid_indx])
    print(ans) 
elif total == mid_val:
    print("sum is equal to middle val")
    ans = {
        mid_indx: mid_val
    }
    print(ans)
else:
    print("sum is less thn middle val")
    ans = tuple(numm[mid_indx + 1:])
    print(ans)