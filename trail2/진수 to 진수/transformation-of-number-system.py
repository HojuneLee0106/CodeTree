a, b = map(int, input().split())
n = input()
if a==0:
    print(0)
else:
    answer=[]
    k=1
    ten=0
    for i in range(len(n)):
        ten = ten * a + int(n[i])
    while ten:
        x=ten%b
        answer.append(x)
        ten//=b
    for i in range(len(answer)):
        print(answer[len(answer)-i-1],end="")
# Please write your code here.