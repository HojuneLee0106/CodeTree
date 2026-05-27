a, b, c = map(int, input().split())
N=a*b*c
def hap(x):
    if x//10==0:
        return x%10
    else:
        return x%10+hap(x//10)
print(hap(N))
# Please write your code here.