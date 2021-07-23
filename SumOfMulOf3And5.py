
num=int(input("Enter the number of elements to be entered:"))
print("nums div by 3 are:")
sumof3=0
for i in range(1,num+1):
    if i%3==0:
        print(i)
        sumof3+=i
print("sum of nums div by 3 is:",+sumof3)

print("nums div by 5 are:")
sumof5=0
for i in range(1,num+1):
    if i%5==0:
        print(i)
        sumof5+=i
print("sum of nums div by 5 is:",+sumof5)

