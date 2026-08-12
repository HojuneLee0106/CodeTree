a = list(map(int, input().split()))
answer=0
ans_1=a[1]-a[0]
ans_2=a[2]-a[1]
answer=max(ans_1, ans_2)
print(answer-1)
# Please write your code here.