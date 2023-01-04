
class Rectangle:
    
    def __init__(self,len,bre):
        assert (len>=0 and bre>=0),'INVALID'
        self.len=len
        self.bre=bre
    def calArea(self):
        temp=self.len*self.bre
        return temp
    def calPerimeter(self):
        temp=2*(self.len+self.bre)
        return temp
l=int(input())
b=int(input())
try:
    ob=Rectangle(l,b)
    peri=ob.calPerimeter()
    Area=ob.calArea()
    print("Area:")
    print(peri)
except AssertionError as o:
    print(o)
   
