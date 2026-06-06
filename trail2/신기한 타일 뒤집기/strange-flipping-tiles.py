from collections import defaultdict
n = int(input())
commands = [tuple(input().split()) for _ in range(n)]
x = []
dir = []
for num, direction in commands:
    x.append(int(num))
    dir.append(direction)
tile=defaultdict(int)
start=0
for i in range(n):
    if dir[i]=="R":
        for j in range(start,start+x[i]):
            tile[j]=1
        start+=(x[i]-1)
    else:
        for j in range(start,start-x[i],-1):
            tile[j]=-1
        start-=(x[i]-1)
black = sum(1 for v in tile.values() if v == 1)
white = sum(1 for v in tile.values() if v == -1)
print(white, black)
# Please write your code here.