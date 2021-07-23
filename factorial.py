num=int(input("Enter the number:"))
fact=1
for i in range(1,num+1):
    print(i)
    result=fact*int(i)
    fact=result
print(result)

