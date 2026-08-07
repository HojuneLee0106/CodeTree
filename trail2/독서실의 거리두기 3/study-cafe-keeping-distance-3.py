N = int(input())
seats = input()
pos=[]
answer=0
for i in range(N):
    if seats[i]=="1":
        pos.append(i)
for i in range(N):
    if i in pos:
        continue
    new_pos=pos[:]
    new_pos.append(i)
    new_pos.sort()
    d=N
    for j in range(len(new_pos)-1):
        new_d=new_pos[j+1]-new_pos[j]
        d=min(d, new_d)
    answer=max(answer, d)
print(answer)
# Please write your code here.