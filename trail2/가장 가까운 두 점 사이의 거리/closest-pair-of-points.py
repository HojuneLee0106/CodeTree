n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x = [p[0] for p in points]
y = [p[1] for p in points]
answer=[]
for i in range(n-1):
    for j in range(i+1,n):
        answer.append((x[i]-x[j])**2+(y[i]-y[j])**2)
print(min(answer))
# Please write your code here.