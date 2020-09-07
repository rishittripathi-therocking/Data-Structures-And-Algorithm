def lcm(x,y):
    greater=0
    if x>y:
        greater=x
    else:
        greater=y
    lc=0
    while(True):
        if(greater%x==0) and (greater%y==0):
            lc=greater
            break
        else:
            greater+=1
    return lc
num1,num2=map(int,input().split())
print(lcm(num1,num2))
