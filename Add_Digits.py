n=int(input())
while(True):
    if len(str(n))==1:
        break
    else:
        k=0
        for i in str(n):
            k+=int(i)
        n=k
print(n)