'''
Return a new set of identical items from two sets
Given:

set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
Expected output:

{40, 50, 30}
'''





set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

print(set1.intersection(set2))




'''

Exercise 3: Get Only unique items from two sets
Write a Python program to return a new set with unique items from both sets by removing duplicates.

Given:

set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
Expected output:

{70, 40, 10, 50, 20, 60, 30}
'''

set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}


print(set1.union(set2))

'''
Given two Python sets, write a Python program to update the first set with items that exist only in the first set and not in the second set.

Given:

set1 = {10, 20, 30}
set2 = {20, 40, 50}
Expected output:

set1 {10, 30}
'''

set3= {10, 20, 30}
set4 = {20, 40, 50}

set3.difference_update(set4)
print(set3)


 

