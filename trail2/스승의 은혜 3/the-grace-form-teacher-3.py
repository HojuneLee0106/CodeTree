N, B = map(int, input().split())
gifts = [tuple(map(int, input().split())) for _ in range(N)]
P = [gift[0] for gift in gifts]
S = [gift[1] for gift in gifts]
T=[[P[i], S[i], P[i]+S[i]]for i in range(N)]
T.sort(key=lambda x:x[2])
answer=0
budget=0
for i in range(N):
    if budget+T[i][2]> B:
        if budget+T[i][0]/2+T[i][1]<=B:
            budget+=(T[i][0]/2+T[i][1])
            answer+=1
    else:
        answer+=1
        budget+=T[i][2]
print(answer)

# Please write your code here.