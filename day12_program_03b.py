set1={10,20,30,40}
set2={60,70,80,90}

if set1.isdisjoint(set2):
    print("two sets have no common elements")
else:
    print("tywo sets have common in elements")
    print(set1.intersection(set2))
