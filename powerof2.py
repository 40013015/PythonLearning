def powerofTwo(num):
    while num%2==0:
        num=num/2
        if num==1:
            return "Given num is power of two"
    return "not power of two"
print(powerofTwo(int(input())))