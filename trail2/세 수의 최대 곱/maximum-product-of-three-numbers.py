n = int(input())
arr = list(map(int, input().split()))
answer=0
arr.sort()
answer=max((arr[0]*arr[1]*arr[-1]),(arr[-1]*arr[-2]*arr[-3]))
print(answer)
# Please write your code here.