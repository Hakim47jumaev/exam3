# def cnt(a,list1):
#     cntt=0
#     for i in range(len(list1)):
#         if a == list1[i]:
#             cntt+=1
#             list1[i]=1111111111111111111111
#     return cntt

# list1=input().split()
# l=len(list1)
# for i in list1:
#     a=cnt(i,list1)
#     print(a) 

list1=input().split()
l=0
k=1
for i in range(0,len(list1),k):
    a=list1.count(list1[i])
    l+=1
    k=a
print(l) 