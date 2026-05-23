n, m = map(int, input().split())
def swap(a,b):
    a,b=b,a
    return a,b
print(*swap(n,m))
# Please write your code here.