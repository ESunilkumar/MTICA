def representlen(s):
    temp=inp.split()
    ans=[]
    for i in temp:
        ans.append(len(i))
        
    return ans

inp=input()
print(*representlen(inp))


# return[len(i) for i in temp]
