a=input("enter a number n:")
print("output:")
try:
    for i in range(1,11):
        print(f"{int(a)} X {i} = {int(a)*i}")

except:
    print("Invalid syntax!")

print("some important notice")
print("end of programme")