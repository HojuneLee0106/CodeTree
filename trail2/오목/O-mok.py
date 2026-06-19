board = [list(map(int, input().split())) for _ in range(19)]
answer=0
dx=[1,1,1,0]
dy=[1,0,-1,-1]
curr=0
answer=0
answer_grid=[]
for i in range(19):
    for j in range(19):
        if board[i][j]!=0:
            for k in range(4):
                x=j
                y=i
                for g in range(4):
                    nx=x+dx[k]
                    ny=y+dy[k]
                    if nx<0 or ny<0 or nx>18 or ny>18:
                        break
                    else:
                        if g==3:
                            if board[y][x]!=board[ny][nx]:
                                break
                            else:
                                answer=board[y][x]
                                answer_x=x-dx[k]
                                answer_y=y-dy[k]
                                answer_grid.append(answer_y+1)
                                answer_grid.append(answer_x+1)
                        if board[y][x]!=board[ny][nx]:
                            break
                        else:
                            x=nx
                            y=ny
if answer!=0:
    print(answer)
    print(*answer_grid)
else:
    print(answer)
# Please write your code here.