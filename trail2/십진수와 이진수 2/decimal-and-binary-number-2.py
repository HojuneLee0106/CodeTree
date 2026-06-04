N = input()
x=1
num=0
for i in range(len(N)):
    if int(N[len(N)-1-i])==1:
        num+=x
        x*=2
    else:
        x*=2
num*=17
answer=[]
if num==0:
    print(0)
else:
    while num:
        answer.append(num%2)
        num//=2
    for i in range(len(answer)):
        print(answer[len(answer)-1-i],end="")
# Please write your code here.