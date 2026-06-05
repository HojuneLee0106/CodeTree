n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]
x=[0 for _ in range(100)]
for i, j in segments:
    for k in range(i-1,j):
        x[k]+=1
print(max(x))        
# Please write your code here.