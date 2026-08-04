pos = list(map(int, input().split()))
pos.sort()
x, y, z = pos[0], pos[1], pos[2]
if y - x == 1 and z - y == 1:
    print(0)
elif y - x == 2 or z - y == 2:
    print(1)
else:
    print(2)
# Please write your code here.