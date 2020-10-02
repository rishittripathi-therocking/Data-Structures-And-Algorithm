# Uses python3
import sys

def binary_search(a, x, l, r):
    left, right = l,r
    # write your code here
    mid=(l+r)//2
    if a[mid]==x:
        return mid
    elif x<a[mid]:
        binary_search(a,x,0,mid-1)
    else:
        binary_search(a,x,mid+1, len(a))

def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1

data = list(map(int, input.split()))
n = data[0]
m = data[n + 1]
a = data[1 : n + 1]
for x in data[n + 2:]:
    # replace with the call to binary_search when implemented
    print(binary_search(a, x, 0, len(a)), end = ' ')
