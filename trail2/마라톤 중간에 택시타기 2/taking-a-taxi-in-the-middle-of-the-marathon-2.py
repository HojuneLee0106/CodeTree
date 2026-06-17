n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x = [p[0] for p in points]
y = [p[1] for p in points]
t=len(x)-2
s=1
answer=[]
for i in range(t):
    distance=0
    s_x=x[0]
    s_y=y[0]
    for j in range(1,n):
        if j==s:
            continue
        else:
            distance+=(abs(s_x-x[j])+abs(s_y-y[j]))
            s_x=x[j]
            s_y=y[j]
    answer.append(distance)
    s+=1
print(min(answer))
# Please write your code here.