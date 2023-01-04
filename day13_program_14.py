'''
adding of two indivisual array
input taken from user


input:
11 22 33 44
1 2 3 4

 output:
 12 24 36 48


input:
1 2 3 4
0 0 0 0

output:
1 2 3 4
'''
temp1=input().split()
temp2=input().split()
ans=[]
for i,j in zip(temp1,temp2):
    ans.append(int(i)+int(j))
        
print(*ans)
