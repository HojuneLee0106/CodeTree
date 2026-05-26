N = int(input())
def fac(x):
    if x==1:
        return 1
    else:
        return x*fac(x-1)
print(fac(N))
# Please write your code here.