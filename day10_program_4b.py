fo=open(r"D:\pythonpractice59\day10a.txt","a")

for i in range(2):
    inpstr=input("enter string:")
    fo.write(inpstr+'\n')
fo.close()
print("written to file:")
