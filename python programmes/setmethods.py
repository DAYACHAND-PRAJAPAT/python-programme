s1={1,2,3,4,5}
s2={4,5,6,7,8}

print(s1.union(s2))

print(s1.intersection(s2))

#s1.update(s2)
#print(s1)

'''s2.update(s1)
print(s2)'''

#s1.intersection_update(s2)
#print(s1)

s3=s1.symmetric_difference(s2)
print(s3)