def cnt(a,list1):
    cntt=0
    for i in range(len(list1)):
        if a == list1[i]:
            cntt+=1
            list1[i]=111111111
    return cntt



my_list=input().split()

big=cnt(my_list[0],my_list)
for i in my_list:
    a=cnt(i,my_list)
    # if a>big:
    #    l=i
    #    big =a
print(a)