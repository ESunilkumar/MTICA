
'''adding additional elements into the set
'''


set1={10,20,30,40}
set2={40,50,60,70}


set1.symmetric_difference_update(set2)
print(set1)





'''
remove items from set1 that are common in both sets
'''
set1={10,20,30,40}
set2={40,50,60,10}
set1.intersection_update(set2)
print(set1.)
