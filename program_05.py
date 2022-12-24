def interchange3and5(n):
    n=str(n)
    n=n.replace('3','.')
    n=n.replace('5','3')
    n=n.replace('.','5')
    return n
inp=int(input("enter number"))
print(interchange3and5(inp))

    
