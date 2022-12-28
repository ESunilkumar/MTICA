def add_five(x):
    temp=x+5
    return temp
nums=[1,22,33,44]
result=list(map(add_five,nums))
print(nums)
print(result)
print('-'*40)
