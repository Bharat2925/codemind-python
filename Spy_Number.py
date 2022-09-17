s=int(input())
a=1
a1=0
while s>0:
    r=s%10
    a=a*r
    a1=a1+r
    s=s//10
if a==a1:
    print("Spy Number")
else:
    print("Not Spy Number")