n, k = map(int, input().split())
arr = list(map(int, input().split()))
answer=[]
for i in range(n-k+1):
    c=0
    for j in range(i,i+k):
        c+=arr[j]
    answer.append(c)
print(max(answer))
# Please write your code here.