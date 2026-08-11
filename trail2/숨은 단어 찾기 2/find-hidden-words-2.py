N, M = map(int, input().split())
arr = [input() for _ in range(N)]
dx=[1,1,1,0,0,-1,-1,-1]
dy=[0,1,-1,1,-1,1,0,-1]
answer=0
for i in range(N):
    for j in range(M):
        if arr[i][j]=="L":
            for k in range(8):
                x=j
                y=i
                pos=True
                for h in range(2):
                    x+=dx[k]
                    y+=dy[k]
                    if x>=M or x<0:
                        pos=False
                        break
                    elif y>=N or y<0:
                        pos=False
                        break
                    elif arr[y][x]!="E":
                        pos=False
                        break    
                if pos==True:
                    answer+=1
print(answer)
# Please write your code here.