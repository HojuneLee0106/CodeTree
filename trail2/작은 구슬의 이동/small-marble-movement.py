n, t = map(int, input().split())
r, c, d = input().split()
r, c = int(r), int(c)
x=c
y=r
dx=[1,-1,0,0]
dy=[0,0,-1,1]
mapper={"R":0, "L":1, "U":2, "D":3}
opp_mapper={0:1, 1:0 , 2:3, 3:2}
move_dir=mapper[d]
c=0
for i in range(t):
    nx=x+dx[move_dir]
    ny=y+dy[move_dir]
    if nx<1 or ny<1 or nx>n or ny>n:
        move_dir=opp_mapper[move_dir]
    else:
        x+=dx[move_dir]
        y+=dy[move_dir]
print(y,x)
# Please write your code here.