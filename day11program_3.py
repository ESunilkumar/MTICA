''' covert given two lists into a dictionary
keys=['ten','twenty','thirty']
values=[10,20,30]
'''

keys=['ten','twenty','thirty']
values=[10,20,30]
d=dict()
for i,j in zip(keys,values):
    d[i]=j
print(d)
