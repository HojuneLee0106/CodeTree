n, t = map(int, input().split())
arr = list(map(int, input().split()))

ans = 0
cnt = 0 

for num in arr:
    if num > t:
        cnt += 1 
        ans = max(ans, cnt)
    else:
        cnt = 0

print(ans)