l=[]
n=int(input())
for i in range(n):
    k=list(map(int,input().split()))
    l.append(k)
c1=0
c2=0
for i in range(n):
    for j in range(n):
        if i==j:
            c1+=l[i][j]
        if i+j==n-1:
            c2+=l[i][j]
p1="Principal Diagonal:{a}"
p2="Secondary Diagonal:{a}"
print(p1.format(a=c1))
print(p2.format(a=c2))