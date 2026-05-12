# wap of multiple of 5 in 4 diff ways 

# usin =g for loop 
print("multiples of 5 are :")
for i in range(1, 51):
    if i % 5 == 0:
        print(i)
        
        
        
# using range 
print("multiples of 5 are :")
for i in range(5, 51, 5):
    print(i)
    
    
    
# using while loop 
i = 5
print("multiples of 5 are :")
while i <= 50:
    print(i)
    i = i + 5