X, Y = map(int, input().split())
dict={1:2, 2:3}
answer=0
for i in range(X,Y+1):
    number={}
    t=0
    while i!=0:
        t+=1
        if i%10 in number:
            number[i%10]+=1
        else:
            number[i%10]=1
        i//=10
    for j in number:
        if len(number)==2 and (number[j]==1 or number[j]==t-1):
            answer+=1
            break
        else:
            break


print(answer)
# Please write your code here.