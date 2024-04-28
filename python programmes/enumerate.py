fruits=["apple","mango","banana","cherry"]

for index,fruit in enumerate(fruits):
    print(index,fruit)
    if index==3:
        print("i like it!")


for index,fruit in enumerate(fruits,start=1):
    print(index,fruit)
    if index==3:
        print("i like it!")