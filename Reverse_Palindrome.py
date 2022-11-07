n=int(input())
while(True):
    n=n+int(str(n)[::-1])
    if str(n)==str(n)[::-1]:
        print(n)
        break