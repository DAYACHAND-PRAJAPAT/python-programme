list=[1,2,3,4,"DAYACHAND",True,"yes"]
print(len(list))

print(type(list))

print(list)

print(list[0:7])

print(list[0:-4])

print(list[6])

print(list[-6])

print(list[0:7:2])

if 1 in list:
    print("yes")
else:
    print("no")

if "DA" in "DAYACHAND":
    print("yes")
else:
    print("no")

lst=[i for i in range(10) ]
print(lst)

lst1=[i*i for i in range(10)]
print(lst1)

lst2=[i*i for i in range(10) if i%2==0]
print(lst2)



