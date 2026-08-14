n = int(input())
c, s = [], []
for _ in range(n):
    ci, si = input().split()
    c.append(ci)
    s.append(int(si))
A=0
B=0
C=0
answer=0
hall=["A","B","C"]
for i in range(n):
    new_hall=[]
    if c[i]=="A":
        A+=s[i]
    elif c[i]=="B":
        B+=s[i]
    else:
        C+=s[i]
    if A==B and B==C:
        new_hall=["A","B","C"]
    elif A==B and A>C:
        new_hall=["A","B"]
    elif A==C and A>B:
        new_hall=["A","C"]
    elif B==C and B>C:
        new_hall=["B","C"]
    elif A>B and A>C:
        new_hall=["A"]
    elif B>A and B>C:
        new_hall=["B"]
    elif C>A and C>B:
        new_hall=["C"]
    
    if new_hall != hall:
        hall=new_hall
        answer+=1
print(answer)
# Please write your code here.