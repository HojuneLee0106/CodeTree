n = int(input())
students = [tuple(map(int, input().split())) + (i + 1,) for i in range(n)]
class Student:
    def __init__(self, height, weight,seq):
        self.height=height
        self.weight=weight
        self.seq=seq
stu=[]
for i in range(n):
    x=Student(students[i][0], students[i][1],i+1)
    stu.append(x)
stu.sort(lambda x:(-x.height,-x.weight))
for i in range(n):
    print(stu[i].height, stu[i].weight, stu[i].seq)
# Please write your code here.
