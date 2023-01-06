def myfunc():
    x='john'
    def myfunc2():
        nonlocal x
        x='hello'
    myfunc2()
    return x
print(myfunc())
