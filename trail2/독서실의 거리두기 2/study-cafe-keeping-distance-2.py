N = int(input())
seats = input()
pos=[]
for i in range(N):
    if seats[i]=="1":
        pos.append(i)
dis=N
for j in range(len(pos)-1):
    dis=min(dis, (pos[j+1]-pos[j]))
answer=0
for j in range(N):
    dis_2=N
    if j in pos:
        continue
    for k in range(len(pos)):
        dis_2=min(dis_2, abs(pos[k]-j))
    answer=max(answer, dis_2)
print(min(answer, dis))

# Please write your code here.