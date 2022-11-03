l=list(map(int,input().split()))
for i in range(max(l[0],l[1]),99999):
    if i%l[0]==0 and i%l[1]==0:
        print(i)
        break