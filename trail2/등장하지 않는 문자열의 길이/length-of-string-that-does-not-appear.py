N = int(input())
str = input()
answer=0
for i in range(1,N+1):
    pos={}
    for j in range(N+1-i):
        if str[j:j+i] not in pos:
            pos[str[j:j+i]]=1
        else:
            pos[str[j:j+i]]+=1
    if max(pos.values())>=2:
        answer=i
print(answer+1)
        
# Please write your code here.