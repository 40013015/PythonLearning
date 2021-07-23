from itertools import permutations
def permute(num):
    perm=set(permutations(str(num),len(str(num))))
    print(perm)

    permutednum=[]
    for nums in perm:
        res=''.join(nums)
        permutednum.append(res)
        new = sorted(permutednum)
    print(permutednum)

    print(new)
    for i in new:
        if str(i)>num:
            return i
print(permute(input("enter:")))

