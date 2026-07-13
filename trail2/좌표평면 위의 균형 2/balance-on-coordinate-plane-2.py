n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
real=[]
for i in range(2,101,2):
    for j in range(2,101,2):
        answer=[0 for _ in range(4)]
        for k in range(n):
            if points[k][0]<i and points[k][1]<j:
                answer[0]+=1
            elif points[k][0]<i and points[k][1]>j:
                answer[1]+=1
            elif points[k][0]>i and points[k][1]<j:
                answer[2]+=1
            else:
                answer[3]+=1
        real.append(max(answer))
print(min(real))
# Please write your code here.