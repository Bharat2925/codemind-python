n=int(input())
l=list(map(int,input().split()))
d=l[n//2:][::-1]+l[:n//2]
for i in d:
    print(i,end=' ')