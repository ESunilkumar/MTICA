def add(*n):
    temp=0
    for i in n:
        temp += i
    return temp
print("add():",add())

print("add(5):",add(5))

print("add(5,7)",add(5,7))
print("add(5,7,2)",add(5,7,2))

print("add(5,7,2,11,13,79)",add(5,7,2,11,13,79))
