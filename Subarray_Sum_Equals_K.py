a=list(map(int,input().split()))
l=list(map(int,input().split()))
f=0
for i in range(len(l)):
    c=0
    for j in range(i,len(l)):
        c+=l[j]
        if c==a[1]:
            f+=1
print(f)