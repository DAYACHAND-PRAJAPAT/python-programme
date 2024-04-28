s1={1,2,3,4,5}
s2={6,7,8,9}
print(s1.isdisjoint(s2))

s3={1,2,3,4,5}
s4={4,5}
print(s3.issuperset(s4))
print(s4.issubset(s3))

s3.add(6)
print(s3)

s3.remove(6)
print(s3)
# we can use discard instead of remove....but discard not through any error
print(s1.pop())

del(s2) # we can delete entire set by using del keyword

s1.clear()
print(s1)