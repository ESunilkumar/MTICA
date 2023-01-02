def printseries(n):
    for i in range(1,n+1):
        num=1
        print()
        for j in range(i):
            print(num,end='')
            num=num+1
inp=int(input())
printseries(inp)
