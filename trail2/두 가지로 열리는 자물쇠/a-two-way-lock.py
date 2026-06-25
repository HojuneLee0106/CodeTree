N = int(input())
a1, b1, c1 = map(int, input().split())
a2, b2, c2 = map(int, input().split())
answer=0
def is_close(x,y,z):
    return abs(x - y) <= 2 or abs(x - y) >= N - 2
for i in range(1,N+1):
    for j in range(1,N+1):
        for k in range(1,N+1):
            cond1 = is_close(i, a1, N) and is_close(j, b1, N) and is_close(k, c1, N)
            cond2 = is_close(i, a2, N) and is_close(j, b2, N) and is_close(k, c2, N)
            if cond1 or cond2:
                answer += 1
print(answer)
# Please write your code here.