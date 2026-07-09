n = int(input())
a = list(map(int, input().split()))
answer=0
for K in range(1,max(a)):
    x=0
    for i in range(n-1):
        for j in range(i+1,n):
            if a[j]-K==K-a[i]:
                x+=1
    answer=max(answer,x)
print(answer)
# Please write your code here.