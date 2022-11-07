n=int(input())
l=list(map(int,input().split()))
d=1
for i in l:
    d*=i
for i in range(max(l),d+1):
    for j in l:
        if i%j!=0:
            break
    else:
        print(i)
        break