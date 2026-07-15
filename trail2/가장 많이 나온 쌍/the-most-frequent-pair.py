n, m = map(int, input().split())
pairs = [tuple(map(int, input().split())) for _ in range(m)]
answer={}
for i in range(m):
    pair=pairs[i]
    x=max(pair)
    y=min(pair)
    pair=(x,y)
    if pair in answer:
        answer[pair]+=1
    else:
        answer[pair]=1
print(max(answer.values()))

# Please write your code here.