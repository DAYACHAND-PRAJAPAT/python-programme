a = int(input("enter a:"))
b = int(input("enter b:"))
c =int(input("enter c:"))  
d = int(input("enter d:"))
largest = a

if b > largest:
    largest = b

if c > largest:
    largest = c

if d > largest:
    largest = d

print("The largest number among", a, ",", b, ",", c, ", and", d, "is:", largest)
