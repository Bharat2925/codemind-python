n=int(input())
lt=list(map(int,input().strip().split()))[:n]
count=0
for i in range(0,n):
    if(lt[i]%2!=0):
        count+=1
if (count<=2):
    print("YES")
else:
    print("NO")