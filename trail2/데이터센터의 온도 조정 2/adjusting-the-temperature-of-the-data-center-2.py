N, C, G, H = map(int, input().split())
ranges = [tuple(map(int, input().split())) for _ in range(N)]
max_work=0
for i in range(-1,1002):
    work=0
    for j in range(N):
        if i<ranges[j][0]:
            work+=C
        elif i>ranges[j][1]:
            work+=H
        else:
            work+=G
    max_work=max(max_work,work)
print(max_work)
# Please write your code here.