x1, y1, x2, y2 = map(int, input().split())
a1, b1, a2, b2 = map(int, input().split())

def intersect(x1,y1,x2,y2,a1,b1,a2,b2):
    if x2<a1:
        return True
    elif a2<x1:
        return True
    elif b2<y1:
        return True
    elif y2<b1:
        return True
    else:
        return False
if intersect(x1,y1,x2,y2,a1,b1,a2,b2):
    print("nonoverlapping")
else:
    print("overlapping")
    # Please write your code here.