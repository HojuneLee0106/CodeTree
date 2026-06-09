n, m = map(int, input().split())

# Process robot A's movements
t = []
d = []
for _ in range(n):
    time, direction = input().split()
    t.append(int(time))
    d.append(direction)

# Process robot B's movements
t_b = []
d_b = []
for _ in range(m):
    time, direction = input().split()
    t_b.append(int(time))
    d_b.append(direction)
pos_A=[0]
pos_B=[0]
for i in range(n):
    if d[i]=="R":
        for j in range(t[i]):
            pos_A.append(pos_A[-1]+1)
    else:
        for j in range(t[i]):
            pos_A.append(pos_A[-1]-1)
for i in range(m):
    if d_b[i]=="R":
        for j in range(t_b[i]):
            pos_B.append(pos_B[-1]+1)
    else:
        for j in range(t_b[i]):
            pos_B.append(pos_B[-1]-1)
answer=0
for i in range(min(len(pos_A), len(pos_B))):
    if i==0:
        continue
    else:
        if pos_A[i]==pos_B[i] and pos_A[i-1]!=pos_B[i-1]:
            answer+=1
for i in range(min(len(pos_A), len(pos_B)),max(len(pos_A), len(pos_B))):
    if len(pos_A)>=len(pos_B):
        if pos_A[i]==pos_B[-1] and pos_A[i-1]!=pos_B[-1]:
            answer+=1
    else:
        if pos_A[-1]==pos_B[i] and pos_A[-1]!=pos_B[i-1]:
            answer+=1
print(answer)
# Please write your code here.