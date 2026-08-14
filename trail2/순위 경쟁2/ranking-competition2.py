n = int(input())
c = []
s = []
for _ in range(n):
    ci, si = input().split()
    c.append(ci)
    s.append(int(si))
hall=["A", "B"]
A=0
B=0
answer=0
for i in range(n):
    if c[i]=="A":
        A+=s[i]
    else:
        B+=s[i]
    new_hall=[]
    if A==B:
        new_hall=["A","B"]
    elif A>B:
        new_hall=["A"]
    else:
        new_hall=["B"]
    if  hall != new_hall:
        answer+=1
        hall=new_hall
print(answer)
# Please write your code here.