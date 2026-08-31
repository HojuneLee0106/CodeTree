n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]
answer=float("inf")
for i in range(n):
    min_x=float("inf")
    max_x=0
    for j in range(n):
        if i==j:
            continue
        min_x=min(min_x,segments[j][0])
        max_x=max(max_x,segments[j][1])
    answer=min(answer, max_x-min_x)
print(answer)
# Please write your code here.