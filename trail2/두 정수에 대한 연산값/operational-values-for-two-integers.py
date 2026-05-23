a, b = map(int, input().split())

def cal(x,y):
    if x>y:
        x+=25
        y*=2
        return x, y
    else:
        x*=2
        y+=25
        return x,y
print(*cal(a,b))
# Please write your code here.