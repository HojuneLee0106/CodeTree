board = [list(input()) for _ in range(10)]
B_x=0
B_y=0
L_x=0
L_y=0
R_x=0
R_y=0
for i in range(10):
    for j in range(10):
        if board[i][j]=="B":
            B_y=i
            B_x=j
        elif board[i][j]=="L":
            L_x=j
            L_y=i
        elif board[i][j]=="R":
            R_x=j
            R_y=i
if (B_x==L_x and B_x==R_x) :
    if (L_y>R_y and R_y>B_y) or (B_y>R_y and R_y>L_y):
        print(abs(B_x-L_x)+abs(B_y-L_y)+1)
    else:
        print(abs(B_x-L_x)+abs(B_y-L_y)-1)
elif (B_y==L_y and B_y==R_y):
    if (L_x>R_x and R_x>B_x) or (B_x>R_x and R_x>L_x):
        print(abs(B_x-L_x)+abs(B_y-L_y)+1)
    else:
        print(abs(B_x-L_x)+abs(B_y-L_y)-1)
else:
    print(abs(B_x-L_x)+abs(B_y-L_y)-1)
# Please write your code here.