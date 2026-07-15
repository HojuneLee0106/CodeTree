n = int(input())
ranges = [tuple(map(int, input().split())) for _ in range(n)]
a, b = zip(*ranges)
a, b = list(a), list(b)
answer=[]
for i in range(1,b[0]):
    if i*2>b[0]:
        break
    x=i*2
    pos=True
    for j in range(n):
        if x<=b[j] and x>=a[j]:
            x*=2
        else:
            pos=False
            break
    if pos==True:
        answer.append(i)
print(min(answer))
# Please write your code here.