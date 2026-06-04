n = int(input())
answer=[]
if n==0:
    print(0)
else:
    while n:
        answer.append(n%2)
        n//=2
for i in range(len(answer)-1,-1,-1):
    print(answer[i],end="")
# Please write your code here.