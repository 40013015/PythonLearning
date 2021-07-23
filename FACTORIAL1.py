def fact(num):
    n=1
    for num1 in range(1,num+1):
        res=n*int(num1)
        n=res

    return n
print(fact(int(input())))