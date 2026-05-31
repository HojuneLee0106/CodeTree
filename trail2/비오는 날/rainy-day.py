n = int(input())
date = []
day = []
weather = []

for _ in range(n):
    d, dy, w = input().split()
    date.append(d)
    day.append(dy)
    weather.append(w)
class W:
    def __init__(self,d,da,we):
        self.d=d
        self.da=da
        self.we=we
answer=[]
for i in range(n):
    f=W(date[i],day[i],weather[i])
    answer.append(f)
answer.sort(key=lambda x:x.d)
for i in range(len(answer)):
    if answer[i].we=="Rain":
        print(answer[i].d,answer[i].da,answer[i].we)
        break
# Please write your code here.