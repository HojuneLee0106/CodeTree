N = int(input())
numbers = list(map(int, input().split()))
even = 0
odd = 0
for num in numbers:
    if num % 2 == 0:
        even += 1
    else:
        odd += 1
while even < odd:
    even += 1
    odd -= 2
if even == odd:
    print(even + odd)
else:
    print(odd * 2 + 1)
# Please write your code here.