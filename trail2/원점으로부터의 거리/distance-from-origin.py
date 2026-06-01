n = int(input())
points=[]
for i in range(n):
    x=list(map(int, input().split()))
    points.append(x)
class point:
    def __init__(self,x,y,seq,man):
        self.x=x
        self.y=y
        self.seq=seq
        self.man=man
dis=[]
for i in range(n):
    x=point(points[i][0], points[i][1],i+1,abs(points[i][0])+abs(points[i][1]))
    dis.append(x)
dis.sort(key=lambda x:(x.man,x.seq))
for i in range(n):
    print(dis[i].seq)
# Please write your code here.
