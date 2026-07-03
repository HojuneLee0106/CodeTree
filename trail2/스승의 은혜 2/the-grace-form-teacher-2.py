N, B = map(int, input().split())
P = [int(input()) for _ in range(N)]
P.sort()
answer=0
money=0
for i in range(N):
    if money+P[i]>B:
        if money+P[i]//2<=B:
            answer+=1
            money+=P[i]//2
        else:
            break
    else:
        answer+=1
        money+=P[i]
print(answer)
# Please write your code here.