num=int(input("Enter the number:"))
res=0
for i in range(1,num+1):
    result=res+int(i)
    res=result
print(res)
