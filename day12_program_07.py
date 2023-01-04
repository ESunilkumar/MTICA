
class Circle:
    from math import pi
    def __init__(self,radius):
        self.radius=radius
        
    def calculatearea(self):
        temp=self.pi*self.radius**2
        return temp
    def calculateperimeter(self):
        temp=2*self.pi*self.radius
        return temp
    
r=int(input())

ob=Circle(r)
area=ob.calculatearea()
peri=ob.calculateperimeter()
print(r,area)
print(r,peri)
    
        
    
