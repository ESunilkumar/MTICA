num1=int(input())
num2=int(input())
try:
    res=num1/num2
except ZeroDivisionError:
    print("divide by zero is not allowed")
else:
    print(num1,'/',num2,'=',res)
print('thanks')
    
