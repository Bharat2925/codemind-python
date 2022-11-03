def isprim(n):
    if n==1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
n=int(input())
n+=1
while(True):
    if str(n)==str(n)[::-1] and isprim(n):
        print(n)
        break
    n+=1