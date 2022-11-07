n=int(input())
l=list(map(int,input().split()))
s=''
for i in l:
    s+=str(i)
s=str(int(s)+1)
for i in s:
    print(int(i),end=' ')