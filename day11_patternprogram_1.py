cmp=input()
inp=int(input())


def Aprintseries(ch,n):
    assert (n>=0),'INVALID'
    for i in range(n):
        print(ch*i)

        
def printseries(ch,n):
    assert (n>=0),'INVALID'
    for i in range(n,0,-1):
        print(ch*i)


try:
    Aprintseries(cmp,inp)
except Exception as ob:
    print(ob)

    
try:
    printseries(cmp,inp)
except Exception as ob:
    print(ob)
