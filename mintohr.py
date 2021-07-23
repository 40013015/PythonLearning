min=int(input())

if min>60:
    hours=min//60
    minutes=min%60
print(str(hours) +":"+str(minutes))
