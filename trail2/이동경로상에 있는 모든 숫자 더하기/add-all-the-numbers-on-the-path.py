N, T = map(int, input().split())
str = input()
board = [list(map(int, input().split())) for _ in range(N)]
dx=[0,1,0,-1]
dy=[-1,0,1,0]
curr=0
x=N//2
y=N//2
answer=board[y][x]
for i in range(len(str)):
    if str[i]=="F":
        nx=x+dx[curr]
        ny=y+dy[curr]
        if nx<0 or ny<0 or nx>=N or ny>=N:
            continue
        else:
            x=nx
            y=ny
            answer+=board[y][x]
    elif str[i]=="R":
        curr+=1
        curr%=4
    else:
        curr+=3
        curr%=4
print(answer)
# Please write your code here.