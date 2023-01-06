def factor(n):
    temp=[]
    for i in range(1,n+1):
        if n%i==0:
            temp.append(i)
    return temp
def findgcd(n1,n2):
    lstn1=factor(n1)
    lstn2=factor(n2)
    s1=set(lstn1)
    s2=set(lstn2)
    ans=list(s1.intersection(s2))
    ans.sort()
    return ans[-1]
print("two numbers")
a=int(input())
b=int(input())
print(findgcd(a,b))
