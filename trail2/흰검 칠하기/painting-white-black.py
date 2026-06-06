from collections import defaultdict

n = int(input())
commands = [tuple(input().split()) for _ in range(n)]
x = []
dir = []
for num, direction in commands:
    x.append(int(num))
    dir.append(direction)

tile = defaultdict(int)
w = defaultdict(int)
b = defaultdict(int)
start = 0

for i in range(n):
    if dir[i] == "R":
        for j in range(start, start + x[i]):
            if tile[j] == -1:
                continue
            if tile[j] == 0:
                b[j] += 1
                tile[j] = 1
            elif tile[j] == 2:
                b[j] += 1
                if b[j] >= 2 and w[j] >= 2:
                    tile[j] = -1
                else:
                    tile[j] = 1
            else:  # tile[j] == 1
                b[j] += 1
                if b[j] >= 2 and w[j] >= 2:
                    tile[j] = -1
        start += (x[i] - 1)

    else:
        for j in range(start, start - x[i], -1):
            if tile[j] == -1:
                continue
            if tile[j] == 0:
                w[j] += 1
                tile[j] = 2
            elif tile[j] == 1:
                w[j] += 1
                if b[j] >= 2 and w[j] >= 2:
                    tile[j] = -1
                else:
                    tile[j] = 2
            else:  # tile[j] == 2
                w[j] += 1
                if b[j] >= 2 and w[j] >= 2:
                    tile[j] = -1
        start -= (x[i] - 1)

black = sum(1 for v in tile.values() if v == 1)
white = sum(1 for v in tile.values() if v == 2)
grey  = sum(1 for v in tile.values() if v == -1)

print(white, black, grey)