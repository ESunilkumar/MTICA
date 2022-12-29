def printseriesIncreasing(ch,n):
    for i in range(1,n+1,1):
        print(ch*i)
def printseriesDecreasing(ch,n):
    for i in range(n,0,-1):
        print(ch*i)


inpch=input("enter character:")
inpnum=int(input())
printseriesIncreasing(inpch,inpnum)
print('-'*40)
printseriesDecreasing(inpch,inpnum)
