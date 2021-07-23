str1=str(input("Enter string:"))
new=str1.replace(" ",'')
nonlet=[]
res=""
for char in new:
    if not char.isalpha():
        nonlet.append(char)
print(nonlet)

for item in nonlet:
    str1=str1.replace(item,'')
print(str1)

wordlist=str1.split()
count=0
for i in wordlist:
    if len(str(i))>count:
        ans=str(i)
        count=len(str(i))
print(ans)
