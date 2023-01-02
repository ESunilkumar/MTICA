''' rename location ascity in the below dictionary
'''
sample_dict={
    "name:":"killy",
    "ages":25,
    "salary":30000,
    "city":"Newyork",
    }
sample_dict['location']=sample_dict.pop('city')
print(sample_dict)




