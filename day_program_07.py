string=input()

ans=[]
for i in string:
    if i in 'AEIOUaeiou':
        ans.append(i)
print(*ans)


str=input()

sun=0
for i in str:
    if i in 'AEIOUaeiou':
        sun += 1
print(sun)
