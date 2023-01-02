
def printseries(n):
    num=1
    for i in range(1,n+1):
        print()
        for j in range(i):
            print(num,end=' ')
            num += 1
inpnum=int(input())
printseries(inpnum)



def printseries(n):
    num=1
    for i in range(1,n+1):
        print()
        for j in range(i):
            print(i,end=' ')
            num += 1
inpnum=int(input())
printseries(inpnum)
