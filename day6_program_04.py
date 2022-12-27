import time
import sys

inpNo = int(input("enter number:"))
start=time.time()
for i in range(inpNo):
    print('i=',i,'i^2=',i*i)
print("time taken by loop:",
      (time.time()-start)*100000)
            
