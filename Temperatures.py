n=int(input())
l=list(map(int,input().split()))
for i in range(len(l)):
    c=1
    for j in range(i+1,len(l)):
        if l[j]>l[i]:
            print(c,end=' ')
            break
        else:
            c+=1
    else:
        print(0,end=' ')