n = int(input())
l = []
r = []
for _ in range(n):
    left, right = map(int, input().split())
    l.append(left)
    r.append(right)
answer=0
for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            pos=True
            if i!=j and j!=k and i!=k:
                for s in range(n):
                    if s==i or s==j or s==k:
                        continue
                    for h in range(s+1,n):
                        if h==i or h==j or h==k:
                            continue
                        if l[s] <= r[h] and l[h] <= r[s]:
                            pos=False
                            break
                if pos==True:
                    answer+=1
            else:
                continue

print(answer)
# Please write your code here.