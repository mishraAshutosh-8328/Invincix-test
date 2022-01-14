
def loadIn(n) :
    if (n <= 0) :
        return 0
 
    lst =[0] * (n+1)
    lst[1] = 1
 
    sm = lst[0] + lst[1]
 
    for i in range(2,n+1) :
        lst[i] = lst[i-1] + lst[i-2]
        sm = sm + lst[i]
        
    return sm


n = int(input())
print(loadIn(n))

