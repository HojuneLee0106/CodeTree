n = int(input())
students = [
    (h, w, i + 1)
    for i, (h, w) in enumerate([tuple(map(int, input().split())) for _ in range(n)])
]
class student:
    def __init__(self, height, weight, seq):
        self.height=height
        self.weight=weight
        self.seq=seq
stu=[]
for i in range(n):
    x=student(students[i][0], students[i][1], i+1)
    stu.append(x)
stu.sort(key=lambda x:(x.height, -x.weight))
for i in range(n):
    print(stu[i].height, stu[i].weight, stu[i].seq)
# Please write your code here.