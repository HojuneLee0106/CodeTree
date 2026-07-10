X, Y = map(int, input().split())
answer=0
for i in range(X,Y+1):
    num=[]
    s=str(i)
    for j in range(len(s)):
        num.append(s[j])
    pos=True
    for j in range(len(num)):
        rev=-(j+1)
        if s[j]!=s[rev]:
            pos=False
            break
    if pos==True:
        answer+=1
print(answer)
# Please write your code here.