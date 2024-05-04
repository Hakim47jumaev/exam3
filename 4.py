my_list=input().split()
for i in range(1,len(my_list)):
    if int(my_list[i])*int(my_list[i-1])>0:
        print(my_list[i-1],my_list[i])
        break