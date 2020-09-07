def gcd(a,b):
    if a==0:
        return b
    else:
        return gcd(b%a,a)
def lcm(a,b):
    gc=0
    if a<b:
        gc=gcd(a,b)
    else:
        gc=gcd(b,a)
    return (a*b)//gc

num1,num2=map(int,input().split())
print(lcm(num1,num2))
