n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x, y = zip(*points)
x, y = list(x), list(y)

def can_cover(pts, lines_used):
    if not pts:
        return True
    if lines_used==3:
        return False
    px, py=pts[0]
    next_pts_x=[p for p in pts if p[0] !=px]
    if can_cover(next_pts_x, lines_used+1):
        return True
    next_pts_y=[p for p in pts if p[1] !=py]
    if can_cover(next_pts_y, lines_used+1):
        return True
    return False
if can_cover(points,0):
    print(1)
else:
    print(0)

# Please write your code here.