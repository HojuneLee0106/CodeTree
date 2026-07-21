N = int(input())
seat = input()
one=[]
for i in range(N):
    if seat[i]=="1":
        one.append(i)
answer=0
for i in range(N-1):
    for j in range(i+1,N):
        if i in one or j in one:
            continue
        new_one=one[:]
        new_one.append(i)
        new_one.append(j)
        new_one.sort()
        d=[]
        for k in range(1,len(new_one)-1):
            d.append(new_one[k]-new_one[k-1])
            d.append(new_one[k+1]-new_one[k])
        answer=max(answer,min(d))

print(answer)
# Please write your code here.