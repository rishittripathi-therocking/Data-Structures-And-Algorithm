n=int(input())
l=list(map(int,input().split()))
max1=l[0]
index=-1
for i in range(0,n):
    if max1<=l[i]:
        max1=l[i]
        index=i
max2=-9999999999
for i in range(0,n):
    if max2<=l[i] and index!=i:
        max2=l[i]
print(max1*max2)
