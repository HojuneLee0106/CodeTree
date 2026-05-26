N = int(input())
def SQ(x):
    if x//10==0:
        return x**2
    else:
        return SQ(x//10)+(x%10)**2
print(SQ(N))
# Please write your code here.