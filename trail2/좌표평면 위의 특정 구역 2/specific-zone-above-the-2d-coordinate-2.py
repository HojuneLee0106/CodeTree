n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x = [p[0] for p in points]
y = [p[1] for p in points]
answer=[]
for i in range(n):
    new_x=[]
    new_y=[]
    for j in range(n):
        if i==j:
            continue
        new_x.append(x[j])
        new_y.append(y[j])
    min_x=min(new_x)
    min_y=min(new_y)
    max_x=max(new_x)
    max_y=max(new_y)
    answer.append((max_x-min_x)*(max_y-min_y))
print(min(answer))
        
# Please write your code here.