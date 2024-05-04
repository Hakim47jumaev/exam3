str1=input()
li=str1.split()
cnt=0
big=0
for i in range(len(li)):
    if len(li[i])>int(big):
        big=len(li[i])
        sl=li[i]
print(sl,big)