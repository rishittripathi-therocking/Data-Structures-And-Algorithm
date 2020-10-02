# Uses python3
import sys

def binary_search(a, x, l, r):
    while l <= r: 
  
        mid = l + (r - l) // 2; 
        if a[mid] == x: 
            return mid 
        elif a[mid] < x: 
            l = mid + 1
        else: 
            r = mid - 1
    return -1

def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1

a=list(map(int,input().split()))
b=list(map(int,input().split()))
n=a[0]
arr=a[1:n+1]

for x in b[1:]:
    # replace with the call to binary_search when implemented
    print(binary_search(arr, x, 0, len(arr)-1), end = ' ')
