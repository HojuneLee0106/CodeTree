n = int(input())
sequence = list(map(int, input().split()))
idx = n - 1
while idx > 0 and sequence[idx - 1] < sequence[idx]:
    idx -= 1
print(idx)
# Please write your code here.