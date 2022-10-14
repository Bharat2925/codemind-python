n=int(input())
a=n+1
s=0
i=1
count=0
while(i<=n):
    if n%i==0:
        count+=1
    i+=1
if count==2:
    print("0")
else:
    while True:
        is_prime = True
        for i in range (2,int(a**0.5)+1):
            if a%i ==0:
                is_prime = False
                break
        if is_prime == True:
            break
        else:
            a+=1
    s=a-n
    a=n-1
    k=0
    while True:
        is_prime = True
        for i in range (2,int(a**0.5)+1):
            if a%i ==0:
                is_prime = False
                break
        if is_prime == True:
            break
        else:
            a-=1
    k=n-a
    if k<=s:
        print(k)
    else:
        print(s)