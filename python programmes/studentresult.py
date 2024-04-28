math_marks=int(input("enter the maths marks:"))
physics_marks=int(input("enter the physics marks:"))
chemistry_marks=int(input("enter the chemistry marks:"))
result = ((math_marks+physics_marks+chemistry_marks)/300)*100
if(result>=40):
    if(math_marks>=33):
       if(physics_marks>=33):
           if(chemistry_marks>=33):
              print("student is passed")
    else:
        print("student is failed")