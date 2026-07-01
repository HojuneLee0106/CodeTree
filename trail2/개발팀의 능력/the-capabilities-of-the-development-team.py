arr = list(map(int, input().split()))
answer=[]
for i in range(4):
    for j in range(i+1,5):
        for k in range(4):
            for v in range(k+1,5):
                for x in range(5):
                    if i==k or i==x or i==v or j==k or j==v or j==x or k==x or v==x:
                        continue
                    team1=arr[i]+arr[j]
                    team2=arr[k]+arr[v]
                    team3=arr[x]
                    diff1=abs(team1-team2)
                    diff2=abs(team2-team3)
                    diff3=abs(team3-team1)
                    if diff1==0 or diff2==0 or diff3==0:
                        continue
                    big=max(team1, team2, team3)
                    small=min(team1, team2, team3)
                    answer.append(big-small)
if len(answer)==0:
    print(-1)
else:
    print(min(answer))
# Please write your code here.