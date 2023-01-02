def findfrequencydict(s):
    findfrequencydict={}
    for i in s:
        if i in findfrequencydict:
            findfrequencydict[i] += 1
        else:
            findfrequencydict[i]=1
    return findfrequencydict

def formatoutput(d):
    for i in sorted(d):
        print(i,d[i])
    return None

n=int(input())
for i in range(n):
    inpstr=input()
    formatoutput(findfrequencydict(inpstr))
