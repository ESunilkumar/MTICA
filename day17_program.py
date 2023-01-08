def removespaces(s):
    ans=[]
    for i in s:
        if i in 'AQZWSXEDCRFVTGBYHNUJMIKLOPazqwsxedcrfvtgbyhnujmiklop0123456789':
            ans.append(i)
    return ''.join(ans)
inp=input()
print(removespaces(inp))
