A, B, C = map(int, input().split())
answer=0
A_c=C//A
B_c=C//B
for i in range(A_c+1):
    for j in range(B_c+1):
        s=A*i+B*j
        if s<=C:
            answer=max(answer,s)
print(answer)
# Please write your code here.