N = int(input())
moves = [tuple(input().split()) for _ in range(N)]
dir = [move[0] for move in moves]
dist = [int(move[1]) for move in moves]
dx=[1,0,-1,0]
dy=[0,1,0,-1]
mapper={"E":0, "N":1, "W":2,"S":3}
x=0
y=0
time=0
pos=-1
for i in range(N):
    for j in range(dist[i]):
        x+=dx[mapper[dir[i]]]
        y+=dy[mapper[dir[i]]]
        time+=1
        if x==0 and y==0 and pos==-1:
            pos=time
            break
if pos!=-1:
    print(pos)
else:
    print(-1)
# Please write your code here.