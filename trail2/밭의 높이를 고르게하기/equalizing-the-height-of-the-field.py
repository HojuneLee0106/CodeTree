N, H, T = map(int, input().split())
arr = list(map(int, input().split()))
answer=[]
for i in range(N-T+1):
    cost=0
    for j in range(i, i+T):
        if arr[j]==H:
            continue
        else:
            cost+=abs(H-arr[j])
    answer.append(cost)
print(min(answer))
# Please write your code here.