N, B = map(int, input().split())
answer=[]
if N==0:
    print(0)
else:
    if B==4:
        while N:
            answer.append(N%4)
            N//=4
    else:
        while N:
            answer.append(N%8)
            N//=8
    for i in range(len(answer)):
        print(answer[len(answer)-i-1],end="")
# Please write your code here.