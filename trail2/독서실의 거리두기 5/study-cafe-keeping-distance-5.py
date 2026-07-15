N = int(input())
seat = input()
pos=[]
answer=[]
for i in range(N):
    if seat[i]=="1":
        pos.append(i)
d=100
for i in range(len(pos)-1):
    d=min(d, pos[i+1]-pos[i])

for i in range(N):
    if i in pos:
        continue
    dis=100
    for j in range(len(pos)):
        dis=min(dis, abs(i-pos[j]))
    answer.append(dis)
if max(answer)>d:
    print(d)
else:
    print(max(answer))

# Please write your code here.