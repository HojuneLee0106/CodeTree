n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x = [p[0] for p in points]
y = [p[1] for p in points]
answer=[]
for i in range(n-2):
    for j in range(i+1,n-1):
        for k in range(j+1,n):
            if y[i]==y[j]:
                if x[k]==x[i] or x[k]==x[j]:
                    answer.append(abs((x[i]*y[j]+x[j]*y[k]+x[k]*y[i])-(x[j]*y[i]+x[k]*y[j]+x[i]*y[k])))
            if y[j]==y[k]:
                if x[i]==x[k] or x[i]==x[j]:
                    answer.append(abs((x[i]*y[j]+x[j]*y[k]+x[k]*y[i])-(x[j]*y[i]+x[k]*y[j]+x[i]*y[k])))
            if y[i]==y[k]:
                if x[j]==x[i] or x[j]==x[k]:
                    answer.append(abs((x[i]*y[j]+x[j]*y[k]+x[k]*y[i])-(x[j]*y[i]+x[k]*y[j]+x[i]*y[k])))
if len(answer)==0:
    print(0)
else:
    print(max(answer))
# Please write your code here.