math_marks=int(input("enter marks:"))
phy_marks=int(input("enter marks:"))
chem_marks=int(input("enter marks:"))
eng_marks=int(input("enter marks:"))
hindi_marks=int(input("enter marks:"))
per=((math_marks+phy_marks+chem_marks+eng_marks+hindi_marks)/500)*100
if(per>=90):
    print("excellent")
elif(per>=80):
    print("you got A grade")
elif(per>=70):
    print("you got B grade")
elif(per>=60):
    print("you got C grade")
elif(per>=50):
    print("you got D grade")
elif(per<50):
    print("you got failed...")