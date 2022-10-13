s=input()
s=s.split(":")
a=(30*int(s[0])-5.5*int(s[1]))
if a<0:
    a=-a
if a>180:
    print(360-a)
else:
    print(a)