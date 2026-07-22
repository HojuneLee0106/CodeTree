N, K = map(int, input().split())
num = [int(input()) for _ in range(N)]
counts={}
for i in range(N):
    is_explode=False
    for j in range(max(0,i-K), min(N,i+K+1)):
        if i==j:
            continue
        if num[i]==num[j]:
            is_explode=True
            break
    if is_explode:
        counts[num[i]]=counts.get(num[i],0)+1
max_count=0
max_num=0
for n, count in counts.items():
    if count>max_count:
        max_count=count
        max_num=n
    elif count==max_count:
        max_num=max(max_num,n)
print(max_num)    

# Please write your code here.