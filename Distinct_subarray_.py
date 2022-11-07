n1=int(input())
n2=int(input())
l=[]
for i in range(n1,n2+1):
    l.append(i)
f=0
for i in range(len(l)):
    c=0
    for j in range(i,len(l)):
        c+=l[j]
        if c%2!=0:
            f+=1
print(f)