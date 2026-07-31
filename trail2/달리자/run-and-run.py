n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
answer=0
for i in range(n-1):
    diff=A[i]-B[i]
    answer+=diff
    A[i+1]+=diff
print(answer)
# Please write your code here.