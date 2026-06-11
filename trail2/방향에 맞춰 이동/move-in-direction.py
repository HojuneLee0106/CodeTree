n = int(input())
moves = [tuple(input().split()) for _ in range(n)]
dir = [move[0] for move in moves]
dist = [int(move[1]) for move in moves]
pos=[0,0]
for i in range(n):
    if dir[i]=="N":
        pos[1]+=dist[i]
    elif dir[i]=="S":
        pos[1]-=dist[i]
    elif dir[i]=="E":
        pos[0]+=dist[i]
    else:
        pos[0]-=dist[i]
print(*pos)
# Please write your code here.