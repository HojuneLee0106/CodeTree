a, b = map(int, input().split())
c, d = map(int, input().split())
small=min(a,b,c,d)
big=max(a,b,c,d)
clean=[0 for _ in range(big+1)]
for i in range(a,b):
    if clean[i]==0:
        clean[i]=1
for j in range(c,d):
    if clean[j]==0:
        clean[j]=1
answer=0
for k in range(small, big+1):
    if clean[k]==1:
        answer+=1
print(answer)
# Please write your code here.