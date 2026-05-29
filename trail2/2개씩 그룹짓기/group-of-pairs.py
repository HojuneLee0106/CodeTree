n = int(input())
nums = list(map(int, input().split()))
nums.sort()
answer=0
for i in range(n):
    num=nums[i]+nums[2*n-i-1]
    if answer<=num:
        answer=num
print(answer)
# Please write your code here.
