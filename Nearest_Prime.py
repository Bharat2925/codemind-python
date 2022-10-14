t=int(input())
for i in range(t):
    n=int(input())
    a=n
    s=0
    i=1
    count=0
    while(i<=n):
        if n%i==0:
            count+=1
        i+=1
    if count==2:
        print(n)
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
        b=n
        k=0
        while True:
            is_prime = True
            for i in range (2,int(b**0.5)+1):
                if b%i ==0:
                    is_prime = False
                    break
            if is_prime == True:
                break
            else:
                b-=1
        k=n-b
        if k<=s:
            print(b)
        else:
            print(a)