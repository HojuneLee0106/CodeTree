n, m = map(int, input().split())
a = list(map(int, input().split()))
left = max(a)
right=sum(a)
answer=right
while left<=right:
    mid=(left+right)//2
    count=1
    current_sum=0
    for num in a:
        if current_sum + num>mid:
            count+=1
            current_sum=num
        else:
            current_sum+=num
    if count<=m:
        answer=mid
        right=mid-1
    else:
        left=mid+1
print(answer)
# Please write your code here.