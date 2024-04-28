dict={'lakhan':1,'chandu':2,'aditya':3,'ashul':4}

print(dict.get('lakhan'))
print(dict.keys())
print(dict.values())

print(dict.items())

for keys,values in dict.items():
    print(f"the value corresponding to the {keys} is {values}")