n = int(input())
a = []
b = []
c = []
for _ in range(n):
    num, cnt1, cnt2 = map(int, input().split())
    a.append(num)
    b.append(cnt1)
    c.append(cnt2)
ans = 0
for i in range(1, 10):
    for j in range(1, 10):
        for k in range(1, 10):
            if i == j or j == k or i == k:
                continue
            possible = True
            for idx in range(n):
                num = a[idx]
                target_cnt1 = b[idx]
                target_cnt2 = c[idx]
                x = num // 100
                y = (num // 10) % 10
                z = num % 10
                my_cnt1, my_cnt2 = 0, 0
                if x == i: my_cnt1 += 1
                if y == j: my_cnt1 += 1
                if z == k: my_cnt1 += 1
                if i == y or i == z: my_cnt2 += 1
                if j == x or j == z: my_cnt2 += 1
                if k == x or k == y: my_cnt2 += 1
                if my_cnt1 != target_cnt1 or my_cnt2 != target_cnt2:
                    possible = False
                    break
            if possible:
                ans += 1
print(ans)