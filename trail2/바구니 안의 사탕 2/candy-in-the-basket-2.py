N, K = map(int, input().split())
MAX_POSITION = 100
arr = [0] * (MAX_POSITION + 1)
for _ in range(N):
    c, p = map(int, input().split())
    arr[p] += c 
max_candy = 0
for i in range(MAX_POSITION + 1):
    current_candy = 0
    start = max(0, i - K)
    end = min(MAX_POSITION, i + K)
    for j in range(start, end + 1):
        current_candy += arr[j]
    if current_candy > max_candy:
        max_candy = current_candy

print(max_candy)
# Please write your code here.