s=input()
l=s.split(',')
l.sort()
def rap(n):
    c=0
    for i in range(1,n+1):
        if n%i==0:
            c+=i
    return c
f=1
for i in l:
    if str(rap(int(i))) in l:
        f=0
        print(i,end=' ')
if f==1:
    print(-1)