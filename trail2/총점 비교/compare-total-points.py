n = int(input())

name = []
score1 = []
score2 = []
score3 = []

for _ in range(n):
    student_input = input().split()
    name.append(student_input[0])
    score1.append(int(student_input[1]))
    score2.append(int(student_input[2]))
    score3.append(int(student_input[3]))

class Student:
    def __init__(self, name, A, B, C):
        self.name=name
        self.A=A
        self.B=B
        self.C=C
stu=[]
for i in range(n):
    x=Student(name[i], score1[i], score2[i], score3[i])
    stu.append(x)
stu.sort(key=lambda x:x.A+x.B+x.C)
for i in range(n):
    print(stu[i].name, stu[i].A, stu[i].B, stu[i].C)
# Please write your code here.