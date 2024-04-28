def func1():
    try:
        l=[1,2,3,4]
        i=int(input("enter the Index:"))
        print(l[i])
        return 1

    except:
        print("some eroee occured!")
        return 0

    finally: # this keyword is used when we want to execute something.....instead of any type of error occured
        print("i am always executed!")

x=func1()
print(x)