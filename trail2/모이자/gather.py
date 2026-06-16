n = int(input())
A = list(map(int, input().split()))
answer=[]
for i in range(n):
    x=0
    for j in range(n):
        x+=(abs(i-j)*A[j])
    answer.append(x)
print(min(answer))
# Please write your code here.