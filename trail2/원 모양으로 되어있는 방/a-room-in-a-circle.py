n = int(input())
a = [int(input()) for _ in range(n)]
room=[0 for _ in range(n)]
answer=[]
start=0
for i in range(n):
    dist_t=0
    for j in range(n):
        if start<=j:
            dist=j-start
            dist_t+=a[j]*dist
        else:
            dist=n-(start-j)
            dist_t+=a[j]*dist
    answer.append(dist_t)
    start+=1
print(min(answer))
# Please write your code here.