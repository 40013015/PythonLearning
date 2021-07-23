l=["0100","1000"]
a,b=list(l[0]),list(l[1])
res=[]
for i in range(len(a)):
    if a[i]=="0" and b[i]=="1":
        x="0"
    elif a[i]=="0" and b[i]=="0":
        x="0"
    else:
        x="0"
    res.append(x)
print("".join(res))