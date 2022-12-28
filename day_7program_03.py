##ans=[]
##for i in range(1,101):
##    if i%2==0 or i%3==0 or i%4==0 or i%5==0 or i%6==0 or i%7==0 or i%8==0 or i%9==0:
##        ans.append(i)
##print(*ans)

##lst=[]
##for i in range(1,1001):
##    for j in range(2,10):
##        if i%j==0:
##            lst.append(i)
##            break
##print(*lst)


ans={i  for i in range(1,101)for j in range(2,10)if  i%j==0   }
print(*ans)
