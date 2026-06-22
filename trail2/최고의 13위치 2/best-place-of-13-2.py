n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

max_coins = 0
for i1 in range(n):
    for j1 in range(n - 2):
        for i2 in range(n):
            for j2 in range(n - 2):
                if i1 == i2 and abs(j1 - j2) < 3:
                    continue
                current_coins = 0
                for k in range(3):
                    current_coins += arr[i1][j1 + k]
                    current_coins += arr[i2][j2 + k]
                max_coins = max(max_coins, current_coins)
print(max_coins)