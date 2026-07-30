N=int(input())
p=[]
for i in range(N):
    l=tuple(map(int, input().split()))
    p.append(l)
cross={}
answer=0
for i in range(N):
    if p[i][0] in cross:
        if cross[p[i][0]]!=p[i][1]:
            answer+=1
            cross[p[i][0]]=p[i][1]
    else:
        cross[p[i][0]]=p[i][1]
print(answer)