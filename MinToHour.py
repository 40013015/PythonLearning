num=int(input())
if num>60:
    minute=num%60
    hour=num//60
result=str(hour)+":"+str(minute)
print(result)
    