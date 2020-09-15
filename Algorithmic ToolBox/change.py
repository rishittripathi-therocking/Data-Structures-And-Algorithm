# Uses python3
import sys

def get_change(m):
    mod10=m%10
    denomination10=(m-mod10)//10
    if mod10<5:
        return denomination10+mod10
    else:
        if mod10==5:
            return denomination10+1
        else:
            denomiantion5=1
            mod10-=5
            return denomination10+denomiantion5+mod10
        #write your code here
    

m=int(input())
print(get_change(m))
