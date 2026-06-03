m1, d1, m2, d2 = map(int, input().split())
days=[0,31,28,31,30,31,30,31,31,30,31,30,31]
when=["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
f=0
s=0
if m1==1:
    f=d1
else:
    for i in range(m1):
        f+=days[i]
    f+=d1
if m2==1:
    s=d2
else:
    for i in range(m2):
        s+=days[i]
    s+=d2
diff=(s-f)
if diff<0:
    print(when[diff%-7])
else:    
    print(when[diff%7])
# Please write your code here.