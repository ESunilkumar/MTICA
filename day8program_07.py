def checkeven(num1):
    if num1%2==0:
        return "even"
    #return None


def checkodd(num1):
    if num1%2==1:
        return "odd"
    #return None

num=int(input())
x=checkeven(num)
y=checkodd(num)

print(x)
print(y)
