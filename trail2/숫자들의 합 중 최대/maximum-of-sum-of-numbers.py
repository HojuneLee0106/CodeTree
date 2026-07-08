X, Y = map(int, input().split())
max_num=0
for i in range(X, Y+1):
    number=[]
    while i>=10:
        number.append(i%10)
        i//=10
    number.append(i)
    max_num=max(max_num,sum(number))
print(max_num)
# Please write your code here.