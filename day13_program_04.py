def demo_yield():
    print("code segment1 is excecuted:")
    x=7
    yield x*x
    print("code segment2 is executed:")
    yield 2
    print("code segment3 is executed:")
    yield 3
    print("code segment4 is executed:")
