a=0
b=1
n=int(input("enter a number n:"))

print(a)
print(b)
i=1
while(i<=n):
    c=a+b
    a=b
    b=c
    i=i+1
    print(c)