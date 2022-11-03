n=int(input())
s=0
for i in str(n**2):
    s+=int(i)
if s==n:
    print("Neon Number")
else:
    print("Not Neon Number")
