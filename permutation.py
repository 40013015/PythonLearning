from itertools import permutations
def permute(num):
    perm=set(permutations(str(num),len(str(num))))
    print(perm)

    permuteNums=[]
    for nums in perm:
        req=''.join(nums)
        permuteNums.append(req)
        res=sorted(permuteNums)
    print(res)

    for i in res:
        if str(i)>num:
            return i
        return -1

print(permute(input("Enter the number:")))