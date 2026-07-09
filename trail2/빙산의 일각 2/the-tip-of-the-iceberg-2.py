n = int(input())
h = [int(input()) for _ in range(n)]
answer=0
for i in range(1,max(h)):
    piece=0
    up=False
    for j in range(n):
        if h[j]>i and up==False:
            up=True
            piece+=1
        elif up==True and h[j]<=i:
            up=False
    answer=max(answer,piece)
print(answer) 
# Please write your code here.