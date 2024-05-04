mlist=input().split()
n=int(input())
cnt=1
for i in mlist:
    if int(i)>=n:
        cnt+=1
print(cnt)