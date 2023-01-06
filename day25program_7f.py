
def outer():
    message='outer function'
    print(message) 
    def inner():
        nonlocal message
        message='inner scope'
        print('inner ;' ,message)
    inner()
    print('outer:',message)

outer()
