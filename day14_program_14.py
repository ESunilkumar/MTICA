class Employee:
    empcount=0
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
        Employee.empcount += 1
    def displaycount(self):
        print("total employee:",Employee.empcount)
    def displayEmployee(self):
        print("name:",self.name,"salary",self.salary)
emp1=Employee("sunilk:",2344447)
emp1.displayEmployee()
emp1.salary=17000
emp1.experience=3

emp1.displayEmployee()
emp1.name="kamalk"
emp1.displayEmployee()
print(emp1.experience)
emp1.displayEmployee()
del emp1.salary
#emp1.displayEmployee()
