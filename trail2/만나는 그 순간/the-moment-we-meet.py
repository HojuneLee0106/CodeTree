n, m = map(int, input().split())
pos_a = [0] 
pos_b = [0]
current_pos = 0
for _ in range(n):
    direction, time = input().split()
    time = int(time)
    
    for _ in range(time):
        if direction == 'R':
            current_pos += 1
        else:
            current_pos -= 1
        pos_a.append(current_pos)
current_pos = 0
for _ in range(m):
    direction, time = input().split()
    time = int(time)
    
    for _ in range(time):
        if direction == 'R':
            current_pos += 1
        else:
            current_pos -= 1
        pos_b.append(current_pos)
answer = -1
min_time = min(len(pos_a), len(pos_b))
for t in range(1, min_time):
    if pos_a[t] == pos_b[t]:
        answer = t
        break

print(answer)