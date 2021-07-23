def poweroftwo(num):
    while num%2==0:
        num=num/2
        if num==1:
            return "num is powe of 2"
    return "num is not"
print(poweroftwo(int(input())))