'''str1=str(input())
print(str1.swapcase())
print(str1.upper())
print(str1.lower())'''

def grtdub(num):
    res=0
    str1=str(num)
    for i in range(len(str1)-1):
        if int(str1[i]+str1[i+1])>res:
            res=int(str1[i]+str1[i+1])
    return res
print(grtdub(int(input())))
