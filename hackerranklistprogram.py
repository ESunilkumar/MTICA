if __name__ == '__main__':
    N = int(input())
    arr=list()
    for i in range(N):
        inp=input().strip().split()
        
        
        if inp[0]=='insert':
            i=int(inp[1])
            e=int(inp[2])
            arr.insert(i,e)
            
        if inp[0]=='print':
            print(arr)
        if inp[0]=='remove':
            e=int(inp[1])
            if e in arr:
                arr.remove(e)
        if inp[0]=='append':
            e=int(inp[1])
            arr.append(e)
        if inp[0]=='sort':
            arr.sort()
        if inp[0]=='pop':
            arr.pop()
        if inp[0]=='reverse':
            arr.reverse()
