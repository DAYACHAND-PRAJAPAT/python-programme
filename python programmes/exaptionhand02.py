try:
    num=int(input("enter a intiger:"))
    a=["daya",4,5,False]
    print(a[num])
except ValueError:
    print("entered value is not an integer")

except IndexError:
    print("Invalid index!")
    
