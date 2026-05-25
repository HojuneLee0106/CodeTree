N = int(input())
c=0
def p(x):
    global c 
    if c==0:
        for i in range(x,0,-1):
            print(i,end=" ")
        c+=1
        return p(x)
    else:
        for i in range(x):
            print(i+1,end=" ")
p(N)
# Please write your code here.