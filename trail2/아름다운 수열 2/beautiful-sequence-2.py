N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
B.sort()
answer_count = 0
for i in range(N - M + 1):
    new_A = A[i:i+M]
    new_A_2 = sorted(new_A)
    if B == new_A_2:
        answer_count += 1
print(answer_count)          
# Please write your code here.