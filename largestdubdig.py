#largest 2 pair
#input:45637264
#output:72

def large(num):
    sum=0
    str1=str(num)
    for i in range(len(str1)-1):
        if int(str1[i]+str1[i+1])>sum:
            sum=int(str1[i]+str1[i+1])
    return sum
print(large(int(input())))


#largest 2 pair
#input:45637264
#output:76
from itertools import permutations
def permute(num):
    perm=set(permutations(str(num),2)) #len(str(num))
    print(perm)

    permutednum=[]
    for nums in perm:
        res=''.join(nums)
        permutednum.append(res)
        new = sorted(permutednum)
    print(permutednum)

    print(new)
    return new[-1]
print(permute(input("enter:")))