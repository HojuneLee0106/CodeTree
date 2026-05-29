n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort()
auth=True
for i in range(n):
    if A[i]!=B[i]:
        auth=False
        break
if auth:
    print("Yes")
else:
    print("No")
# Please write your code here.