n1=int(input())
n2=int(input())
for i in range(n1,n2+1):
    if i%10!=0:
        for j in str(i):
            if i%int(j)!=0:
                break
        else:
            print(i,end=' ')
