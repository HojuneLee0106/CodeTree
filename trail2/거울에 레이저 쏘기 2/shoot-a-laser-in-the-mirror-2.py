n = int(input())
grid = [list(input()) for _ in range(n)]
k = int(input())

dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]

if k <= n:
    r = 0
    c = k - 1
    d = 0
elif k <= 2 * n:
    r = k - n - 1
    c = n - 1
    d = 3
elif k <= 3 * n:
    r = n - 1
    c = 3 * n - k
    d = 2
else:
    r = 4 * n - k
    c = 0
    d = 1

answer = 0

while True:

    answer += 1

    if grid[r][c] == '\\':
        if d == 0: d = 1
        elif d == 1: d = 0
        elif d == 2: d = 3
        elif d == 3: d = 2
    else: 
        if d == 0: d = 3
        elif d == 1: d = 2
        elif d == 2: d = 1
        elif d == 3: d = 0
    r += dr[d]
    c += dc[d]
    if r < 0 or r >= n or c < 0 or c >= n:
        break

print(answer)