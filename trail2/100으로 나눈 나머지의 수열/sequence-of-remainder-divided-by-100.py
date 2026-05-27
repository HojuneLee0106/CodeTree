N = int(input())
def cal(x):
    if x==1:
        return 2
    elif x==2:
        return 4
    else:
        return cal(x-1)*cal(x-2)%100
print(cal(N))
# Please write your code here.