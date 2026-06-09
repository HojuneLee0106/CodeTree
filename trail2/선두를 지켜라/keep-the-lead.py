n, m = map(int, input().split())

# Process A's movements
v = []
t = []
for _ in range(n):
    vi, ti = map(int, input().split())
    v.append(vi)
    t.append(ti)

# Process B's movements
v2 = []
t2 = []
for _ in range(m):
    vi, ti = map(int, input().split())
    v2.append(vi)
    t2.append(ti)
pos_A=[0]
pos_B=[0]

for i in range(n):
    for j in range(1,t[i]+1):
        pos_A.append(pos_A[-1]+v[i])
for i in range(m):
    for j in range(1,t2[i]+1):
        pos_B.append(pos_B[-1]+v2[i])
curr=""
answer=0
c=0
for i in range(len(pos_A)):
    if answer==0 and c==0:
        if pos_A[i]>pos_B[i]:
            curr="A"
            c+=1
        elif pos_B[i]>pos_A[i]:
            curr="B"
            c+=1
    else:
        if pos_A[i]>pos_B[i] and curr=="B":
            answer+=1
            curr="A"
        elif pos_B[i]>pos_A[i] and curr=="A":
            answer+=1
            curr="B"
print(answer)
