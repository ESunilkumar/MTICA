'''Create a dictionary by extracting the keys from a given dictionary
Write a Python program to create a new dictionary by extracting the mentioned keys from the below dictionary.

sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"}

# Keys to extract
keys = ["name", "salary"]


'''

sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"}

# keys to extract
keys = ["name", "salary"]

res=dict()
for i in keys:
    res[i]=sample_dict[i]
print(res)


newdict={
    i:sample_dict[i] for i in keys }
print(newdict)


for k in keys:
    res.update({k:sample_dict[k]})
print(res)
