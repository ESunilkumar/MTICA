def checkevenodd(num1):
    assert(num>0),"negetive numbers"
    if num1%2==0:
        return "even"
    else:
        return "odd"
    
for i in range(3):
    num=int(input())
    try:
        print(num,'is', checkevenodd(num))
    except AssertionError:
        print("error is handled")
