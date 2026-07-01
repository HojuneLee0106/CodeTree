ability = list(map(int, input().split()))

ability.sort()
answer=[]
for i in range(3):
    answer.append(ability[i]+ability[5-i])
print(max(answer)-min(answer))
# Please write your code here.