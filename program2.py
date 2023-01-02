def dictionary(s):
    dictionary={}
    for i in s:
        if i in dictionary:
            dictionary[i] += 1
        else:
            dictionary[i]=1
    return dictionary

def formula(f):
    for i in sorted(f):
        print(i,f[i])
    return None

n=int(input())
for i in range(n):
    inp=input()
    formula(dictionary(inp))
    
