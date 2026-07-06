k, n = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(k)]
answer={}
for i in range(k):
    for j in range(n-1):
        for r in range(j+1,n):
            if (arr[i][j], arr[i][r]) not in answer:
                answer[(arr[i][j], arr[i][r])]=1
            else:
                answer[(arr[i][j], arr[i][r])]+=1
total=0
for i in answer:
    if answer[i]==k:
        total+=1
print(total)
# Please write your code here.