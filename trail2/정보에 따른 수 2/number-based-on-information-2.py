T, a, b = map(int, input().split())
c = []
x = []
for _ in range(T):
    char, pos = input().split()
    c.append(char)
    x.append(int(pos))
def distinct_S(pos):
    min_distinct=2000
    dis=0
    for i in range(T):
        if c[i]=="S":
            dis=abs(x[i]-pos)
            min_distinct=min(min_distinct, dis)
    return min_distinct
def distinct_N(pos):
    dis=0
    min_distinct=2000
    for i in range(T):
        if c[i]=="N":
            dis=abs(x[i]-pos)
            min_distinct=min(min_distinct, dis)
    return min_distinct
answer=0
for i in range(a,b+1):
    if distinct_S(i)<=distinct_N(i):
        answer+=1
print(answer)
# Please write your code here.