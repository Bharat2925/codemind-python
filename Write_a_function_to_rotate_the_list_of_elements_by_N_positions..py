n=int(input())
l=list(map(int,input().split()))
k=int(input())
if k>=n:
    k=k%n
d=l[n-k:]+l[:n-k]
for i in d:
    print(i,end=' ')