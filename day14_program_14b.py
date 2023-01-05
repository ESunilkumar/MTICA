class Employee:
    empcount=0
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
        Employee.empcount += 1
    def displaycount(self):
        print("total employee %d" % Employee.empcount)
    def displayEmployee(self):
        print("name:",self.name,"salary",self.salary)
emp1=Employee("sunilk",9999)
emp1.displayEmployee()
print("is salary an attribute:",hasattr(emp1,'salary'))
print(getattr(emp1,'salary'))
setattr(emp1,'salary',7000)
print('modified salary',getattr(emp1,'salary'))
print(hasattr(emp1,'desg'))
setattr(emp1,'desg','manager')
print(hasattr(emp1,'desg'))
print('added attribute',getattr(emp1,'desg'))
delattr(emp1,'salary')
print("is salary an attribute:",hasattr(emp1,'salary'))
