import sys

def check_carry_free(a, b, c):
    while a > 0 or b > 0 or c > 0:
        digit_sum = (a % 10) + (b % 10) + (c % 10)
        if digit_sum >= 10:
            return False
        a //= 10
        b //= 10
        c //= 10
        
    return True
n = int(sys.stdin.readline())
nums = [int(sys.stdin.readline()) for _ in range(n)]
max_sum = -1
for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            if check_carry_free(nums[i], nums[j], nums[k]):
                current_sum = nums[i] + nums[j] + nums[k]
                max_sum = max(max_sum, current_sum)
print(max_sum)