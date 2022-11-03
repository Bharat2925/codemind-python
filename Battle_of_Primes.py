n1=int(input())
n2=int(input())
def ispr(n):
    if n==1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
c=n1+n2+1
while(True):
    if ispr(c):
        break
    c+=1
print(c-n1-n2)