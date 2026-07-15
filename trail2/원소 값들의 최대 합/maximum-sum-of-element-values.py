n, m = map(int, input().split())
arr = [0] + list(map(int, input().split()))
answer=[]
for i in range(1,n+1):
    total=0
    curr=i
    for j in range(m):
        total+=arr[curr]
        curr=arr[curr]
    answer.append(total)
print(max(answer))
# Please write your code here.