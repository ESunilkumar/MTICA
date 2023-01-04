def square(x=0):
    while x<10:
        x=x+1
        yield x*x
yieldlist=[i for i in square()]
print(yieldlist)



yieldlist=list(square())
print(*yieldlist)
