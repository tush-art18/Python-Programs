# 1. Write a Python program to sum all the items in a list.

#Approach 1
#-----------------------
lst = [7,15,10,11,1,23]
print(lst)
print("-"*35)
print("Sum of all items in the list :", sum(lst))

#-----------------------
#Approach 2
#-----------------------
#-----------------------
lst1 = [7,15,10,11,1,23]
tot = 0
for num in lst1:
    tot += num
print("Sum of all items in the list :", tot)