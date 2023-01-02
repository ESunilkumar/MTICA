
def printseriesIncreasing(ch,n):
    assert isinstance(ch,str),'first arguement is a an string type'
    assert isinstance(n,int),'second arguement should be an integer'
    for i in range(0,n+1,1):
        print(ch*i)

        
def printseriesDecreasing(ch,n):
    assert isinstance(ch,str),'first arguement is a an string type'
    assert isinstance(n,int),'second arguement should be an integer'
    for i in range(n,0,-1):
        print(ch*i)



inpch=input("")
inpnum=int(input(""))


try:
    printseriesIncreasing(inpch,inpnum)
except Exception as ob:
    print(ob)
    
try:
    printseriesDecreasing(inpch,inpnum)
except Exception as ob:
    print(ob)
    
    
