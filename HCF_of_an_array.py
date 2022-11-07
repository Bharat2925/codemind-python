n=int(input())
l=list(map(int,input().split()))
for i in range(min(l)+1,0,-1):
    for j in l:
        if j%i!=0:
            break
    else:
        print(i)
        break