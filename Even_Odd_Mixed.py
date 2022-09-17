n=int(input())
count_e=0
count_o=0
while n>0:
    r=n%10
    if r%2==0:
        count_e+=1
    else:
        count_o+=1
    n=n//10
if count_e!=0 and count_o==0:
    print('Even')
elif count_e==0 and count_o!=0:
    print('Odd')
else:
    print('Mixed')