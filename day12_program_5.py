class Student:
    college='MTICA'
    course='MCA'
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno
    def displaystudent(self):
        print("name:",self.name.title(),"\nrollno",self.rollno)
        print("college:",self.college,"\ncourse:",self.course)
lstobs=[]
for i in range(5):
    n=input()
    inp=int(input())
    temp='obs'+str(i)
    print(temp)
    
    temp=Student(n,inp)
    
    lstobs.append(temp)
for i in lstobs:
    i.displaystudent()
    
