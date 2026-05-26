N = int(input())
def hJ(x):
    if x==2:
        return 2
    elif x==1:
        return 1
    else:
        if x%2==0:
            return x+hJ(x-2)
        else:
            return x+hJ(x-2)
print(hJ(N))
# Please write your code here.