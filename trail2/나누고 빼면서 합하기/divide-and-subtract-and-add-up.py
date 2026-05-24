n, m = map(int, input().split())
A = list(map(int, input().split()))
def check(x,y,L):
    sum=0
    while y!=1:
        if y%2==0:
            sum+=L[y-1]
            y//=2
        else:
            sum+=L[y-1]
            y-=1
    sum+=L[0]
    return sum
print(check(n,m,A))
# Please write your code here.