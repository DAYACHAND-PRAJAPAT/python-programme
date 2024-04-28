x=int(input("enter a number x:"))
match x:
    case 0:
        print("the value of x is zero")
    case 1:
        print("the value of x is one")
    case 2:
        print('the value of x is two')
    case _ if x!=3:
        print(x,"is not 3")
    case _ if x!=4:
        print(x,"is not 4")


