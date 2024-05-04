listt=input().split()
small=999999
for i in listt:
    if int(i)<int(small) and int(i)%2!=0:
        small=i
print(small)