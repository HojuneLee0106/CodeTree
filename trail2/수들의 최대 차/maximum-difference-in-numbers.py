N, K = map(int, input().split())
arr = [int(input()) for _ in range(N)]
min_num=min(arr)
max_num=max(arr)
answer=0
for i in range(min_num, max_num+1):
    if i not in arr:
        continue
    arr_s=[]
    arr_b=[]
    for j in arr:
        if abs(i-j)>K:
            continue
        elif i==j:
            arr_s.append(j)
            arr_b.append(j)
        elif i>j:
            arr_s.append(j)
        else:
            arr_b.append(j)
    answer=max(answer,len(arr_s),len(arr_b))
print(answer)
# Please write your code here.