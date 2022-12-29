def fact(n):
    assert (isinstance(n,int)),"factorial of  non integer numbers is not defined:"
    assert (n>=0),"factorial of negative number is not defined"
   
    if n==0:
        return 1
    else:
        return n*fact(n-1)
try:
    print(fact(-3))
except Exception as ob:
    print(ob)
    
try:
    print(fact(45))
except Exception as ob:
    print(ob)
    
try:
    print(fact(7.5))
except Exception as ob:
    print(ob)

try:
    print(fact("today"))
except Exception as ob:
    print(ob)
