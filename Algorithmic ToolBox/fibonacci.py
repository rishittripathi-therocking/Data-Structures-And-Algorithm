# Uses python3
def calc_fib(n):
    if (n <= 1):
        return n
        
    else:
        l=[0 for i in range(0,n)]
        l[0]=1
        l[1]=1
        if n==2:
            return 1
        else:
            for i in range(2,n):
                l[i]=l[i-1]+l[i-2]
            return (l[n-1])
            

n = int(input())
print(calc_fib(n))
