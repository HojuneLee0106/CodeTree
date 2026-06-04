m1, d1, m2, d2 = map(int, input().split())
A = input()
days=[0,31,29,31,30,31,30,31,31,30,31,30,31]
d={"Mon":0,"Tue":1,"Wed":2,"Thu":3,"Fri":4,"Sat":5,"Sun":6}
day1=0
day2=0
for i in range(m1):
    day1+=days[i]
day1+=d1
for i in range(m2):
    day2+=days[i]
day2+=d2
answer=0
diff=day2-day1
answer+=diff//7
if d[A]<=diff%7:
    answer+=1
print(answer)
# Please write your code here.