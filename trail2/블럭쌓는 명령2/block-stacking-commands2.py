n, k = map(int, input().split())
commands = [tuple(map(int, input().split())) for _ in range(k)]
block=[0 for _ in range(n)]
for i, j in commands:
    for k in range(i-1,j):
        block[k]+=1
print(max(block))
# Please write your code here.