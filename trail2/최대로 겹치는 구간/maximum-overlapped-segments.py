n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]
N=[0 for _ in range(200)]
for i,j in segments:
    for k in range(i,j):
        N[99+k]+=1
print(max(N))
# Please write your code here.