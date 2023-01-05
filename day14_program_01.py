'''
reverse string by split the input and perform output
checks casessee

Input:
grapes orange

output:
separg egnaro
'''



def reversestring(s):
    ans=[i[::-1] for i in s]
    return ans
inp=input().split()
print(*reversestring(inp))
