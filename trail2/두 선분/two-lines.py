x1, x2, x3, x4 = map(int, input().split())
answer=True
line_1=[]
for i in range(x1, x2+1):
    line_1.append(i)
for j in range(x3,x4+1):
    if j in line_1:
        answer=False
        break
if not answer:
    print("intersecting")
else:
    print("nonintersecting")
# Please write your code here.