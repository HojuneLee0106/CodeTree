n = int(input())
moves = [tuple(map(int, input().split())) for _ in range(n)]
a, b, c = zip(*moves)
a, b, c = list(a), list(b), list(c)
answer=[]
for i in range(3):
    hidden=0
    if i==0:
        hidden=1
    elif i==1:
        hidden=2
    else:
        hidden=3
    co=0
    for j in range(n):
        if hidden==a[j]:
            hidden=b[j]
        elif hidden==b[j]:
            hidden=a[j]
        
        if c[j]==hidden:
            co+=1
    answer.append(co)
print(max(answer))

# Please write your code here.