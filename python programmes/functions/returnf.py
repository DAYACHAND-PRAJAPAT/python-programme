def average(*numbers):
    sum=0
    for i in numbers:
        sum=sum+i
    return sum/len(numbers)
c=average(1,2,3,4,5,6,7,8,9)
print(c)
