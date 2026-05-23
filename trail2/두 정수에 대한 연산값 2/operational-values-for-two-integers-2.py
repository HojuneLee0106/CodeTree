a, b = map(int, input().split())
def check(x,y):
    if x>y:
        return x*2,y+10
    else:
        return x+10,y*2
print(*check(a,b))
# Please write your code here.