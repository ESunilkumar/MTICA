''' Merge two Python dictionaries into one
dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
Expected output:

{'Ten': 10, 'Twenty': 20, 'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

'''
dict1={'ten':10,'twenty':20,'thirty':30,'fourty':40}
dict2={'fourty':40,'fifty':50,'sixty':60}
dict3={**dict1,**dict2}
print(dict3)



dict3=dict1.copy()

dict3.update(dict2)
print(dict3)
print(dict3)
