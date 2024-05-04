def cnt(a,list1):
    cntt=0
    for i in range(len(list1)):
        if a == list1[i]:
            cntt+=1
            list1[i]=1111111111111111111111
    return cntt

list1=input().split()
for i in list1:
    a=cnt(i,list1)
    if a==1:
        print(i)
