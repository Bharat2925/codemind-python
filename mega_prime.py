def isprim(n):
    if n==1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
n=int(input())
if isprim(n):
    for i in str(n):
        if isprim(int(i))==False:
            print("Not Mega Prime")
            break
    else:
        print("Mega Prime")
else:
    print("Not Mega Prime")