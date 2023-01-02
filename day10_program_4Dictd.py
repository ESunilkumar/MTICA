'''In Python, we can initialize the keys with the same values.

Given:

employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}
Expected output:

{'Kelly': {'designation': 'Developer', 'salary': 8000}, 'Emma': {'designation
'''
employees = ['Venkatesh', 'Amruth']
defaults = {"designation": 'Developer', "salary": 8000}
data=dict.fromkeys(employees,defaults)
print(data)


print(data["Venkatesh"])

    
