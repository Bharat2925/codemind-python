n=int(input())
if '6' not in str(n):
    print(n)
else:
    p=""
    c=0
    n=str(n)
    for i in range(len(n)):
        if n[i]=='6' and c==0:
            p+='9'
            c+=1
        else:
            p+=n[i]
    print(int(p))
