# Uses python3
import sys

def get_majority_element(a, left, right):
    a.sort()
    cnt=1
    for i in range(1,right):
        if a[i-1]!=a[i]:
            if cnt>right/2:
                return True
            cnt=0
        else:
            cnt+=1
    return False


n=int(input())
a = list(map(int, input().split()))
if get_majority_element(a, 0, n) :
    print(1)
else:
    print(0)
