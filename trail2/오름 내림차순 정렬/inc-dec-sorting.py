n = int(input())
nums = list(map(int, input().split()))
nums.sort()
print(*nums)
nums.sort(reverse=True)
print(*nums)
# Please write your code here.
