t=int(input())
for k in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    d=l[0]
    if l[0]>l[1]:
        c=1
    else:
        c=0
    for i in range(len(l)-1):
        if l[i]>d and l[i]>l[i+1]:
            c+=1
        d=max(d,l[i])
    if l[len(l)-1]>d:
        c+=1
    s="Case #{t}: {p}"
    print(s.format(t=k+1,p=c))