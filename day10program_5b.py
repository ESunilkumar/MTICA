'''remove keys fron dict

sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"}

# Keys to remove
keys = ["name", "salary"]'''




sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"}

# keys to remove
keys = ["name", "salary"]


for i in keys:
    sample_dict.pop(i)
print(sample_dict)


d=dict()
for i in sample_dict.keys()-keys:
    d[i]=sample_dict[i]
print(d)


#dict comprehension 
sample_dict = {k: sample_dict[k] for k in sample_dict.keys() - keys}
print(sample_dict)

