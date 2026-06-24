n = int(input())
arr = [0] * 101
for _ in range(n):
    pos, alpha = input().split()
    arr[int(pos)] = alpha
max_size = 0
for start in range(1, 101):
    for end in range(start, 101):
        if arr[start] == 0 or arr[end] == 0:
            continue
        c_G = 0
        c_H = 0
        for k in range(start, end + 1):
            if arr[k] == 'G':
                c_G += 1
            elif arr[k] == 'H':
                c_H += 1
        if c_G == 0 or c_H == 0 or c_G == c_H:
            size = end - start
            if size > max_size:
                max_size = size
print(max_size)