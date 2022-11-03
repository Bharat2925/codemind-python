n1=int(input())
def ispr(n):
    if n==1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
c=0
for i in range(1,n1+1):
    if ispr(i)==False and n1%i==0:
        c+=1
print(c)