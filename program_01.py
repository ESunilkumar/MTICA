student=[[98,"sunilkumar",99,90],[97,"anilkumar",98,99],[96,"amalamma",99,99],[100,"arshitha",100,100]]
student.sort()
print(student)

student.sort(key=lambda temp:temp[2])
print(student)
student.sort(key=lambda temp:temp[3])
print(student)
student.sort(key=lambda  temp:temp[1])
print(student)
student.sort(key=lambda temp:temp[0])
print(student)0
