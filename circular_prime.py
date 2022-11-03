def isprim(n):
    if n==1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
n=int(input())
if isprim(n):
    if isprim(int(str(n)[::-1])):
        print("circular prime")
    else:
        print("prime but not a circular prime")
else:
    print("not prime")