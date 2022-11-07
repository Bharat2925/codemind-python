k=[]
n=int(input())
l=list(map(int,input().split()))
l.sort()
for i in range(len(l)-1):
    if l[i]!=l[i+1]:
        print(l[i],end=' ')
print(l[n-1])