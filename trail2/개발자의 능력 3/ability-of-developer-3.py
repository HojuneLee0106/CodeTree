abilities = list(map(int, input().split()))
total=sum(abilities)
answer=[]
for i in range(4):
    for j in range(i+1,5):
        for k in range(j+1,6):
            hap=abilities[i]+abilities[j]+abilities[k]
            rest=total-hap
            diff=abs(hap-rest)
            answer.append(diff)
print(min(answer))
# Please write your code here.