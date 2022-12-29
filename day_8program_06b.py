num1=input()
num2=input()
try:
    res=int(num1)/int(num2)
except (ZeroDivisionError,ValueError):
    print("exception handled by programmer")
except Exception as ob:
    print(ob)
else:
    print(num1,'/',num2,'=',res)
finally:
    print("thanks")
print('thanks and visit again')
    
