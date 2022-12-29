def div(a,b):
    assert (b!=0),"divided by zero is not defined"
    return a/b
try:
    print(div(30,0))
except AssertionError as obj:
    print(obj)
try:
    print(div(40,'hello'))
except Exception as obj:
    print(obj)
try:
    print(div(100,4))
except Exception as obj:
    print(obj)
