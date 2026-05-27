N = int(input())
def cal(x):
    if x==1:
        return 1
    elif x==2:
        return 2
    else:
        return cal(x//3)+cal(x-1)
print(cal(N))
# Please write your code here.