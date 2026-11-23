a=int(input("enter a:"))
b=int(input("enter b:"))
c=int(input("enter c:"))
d= int(input("enter d:"))

if a>b and a>c and a>d:
    print(a,"is large")
elif b>a and b>c and b>d:
    print(b,"is large")
elif c>a and c>b and c>d:
    print(c,"is large")
else:
    print(d,"is large")