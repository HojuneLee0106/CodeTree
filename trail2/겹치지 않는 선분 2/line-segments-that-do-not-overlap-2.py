n = int(input())
lines = [tuple(map(int, input().split())) for _ in range(n)]
answer=0
for i in range(n):
    pos=True
    for j in range(n):
        if i==j:
            continue
        if lines[i][0]<=lines[j][0] and lines[j][1]<=lines[i][1]:
            pos=False
            break
        if lines[i][0]>=lines[j][0] and lines[j][1]>=lines[i][1]:
            pos=False
            break
    if pos==True:
        answer+=1
print(answer)    
# Please write your code here.