n = int(input())
name = []
korean = []
english = []
math = []

for _ in range(n):
    student_info = input().split()
    name.append(student_info[0])
    korean.append(int(student_info[1]))
    english.append(int(student_info[2]))
    math.append(int(student_info[3]))
class Student:
    def __init__(self, name, kor, eng, math):
        self.name=name
        self.kor=kor
        self.eng=eng
        self.math=math
stu=[]
for i in range(n):
    x=Student(name[i], korean[i], english[i],math[i])
    stu.append(x)
stu.sort(key=lambda x:(-x.kor, -x.eng, -x.math))
for i in range(n):
    print(stu[i].name, stu[i].kor, stu[i].eng, stu[i].math)
# Please write your code here.