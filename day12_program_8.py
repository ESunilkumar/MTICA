class Number:
    def __init__(self,n):
        self.n=n
    def calculateFactorial(self):
        if self.n==0:
            return 1
        res=1
        for i in range(1,self.n +1):
            res *=i
        return res
    def checkeven(self):
        if self.n%2==0:
            return "even"
        else:
            return "odd"
    def sumofdigits(self):
        if self.n<0:
            self.n=abs(self.n)
            
        temp=str(self.n)
        t=0
        for i in temp:
            t += int(i)
        return t
    def Armstrong(self):
        str1=str(self.n)
        total=0
        for i in str1:
            total += int(i)**len(str1)
        if inp==total:
            return 1
        else:
            return 0

    def checkprime(self):
        assert self.n>=1,'INVALID'
        if self.n==1 or self.n==2 or self.n==3:
            for i in range(2,self.n):
                if self.n%i==0:
                    return "not a prime"
            return "prime"
                
            
        
inp=int(input())
obj=Number(inp)

print("Factorial of ",inp,"is",obj.calculateFactorial())
print(inp,"is",obj.checkeven())
print('sum of digits of',inp,'is',obj.sumofdigits())
print('armstrong',inp,'is',obj.Armstrong())

print('prime',inp,'is',obj.checkprime())
try:
    print('prime',inp,'is',obj.checkprime())
except AssertionError as b:
    print(b)

