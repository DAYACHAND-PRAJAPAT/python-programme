a=[1,2,3,4]
i=int(input("enter the index:"))

if(i<0 or i>3):
    raise IndexError("the value should be in range of 0 to 5")
