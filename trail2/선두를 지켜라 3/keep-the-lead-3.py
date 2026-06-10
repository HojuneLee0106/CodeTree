N, M = map(int, input().split())

# Process A's movements
v = []
t = []
for _ in range(N):
    vi, ti = map(int, input().split())
    v.append(vi)
    t.append(ti)

# Process B's movements
v2 = []
t2 = []
for _ in range(M):
    vi, ti = map(int, input().split())
    v2.append(vi)
    t2.append(ti)
hall=["AB"]
A=[0]
B=[0]
answer=0
for i in range(N):
    for j in range(t[i]):
        A.append(A[-1]+v[i])
for i in range(M):
    for j in range(t2[i]):
        B.append(B[-1]+v2[i])
for i in range(1,sum(t)+1):
    if A[i]==B[i]:
        if hall[-1]!="AB":
            answer+=1
            hall.append("AB")
    elif A[i]>B[i]:
        if hall[-1]!="A":
            answer+=1
            hall.append("A")
    else:
        if hall[-1]!="B":
            answer+=1
            hall.append("B")
print(answer)
# Please write your code here.