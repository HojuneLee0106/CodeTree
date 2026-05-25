n = int(input())
c=0
def p(x):
    global c
    if c==0:
        for i in range(x,0,-1):
            for j in range(i,0,-1):
                print("*",end=" ")
            if i!=1:
                print()
        c+=1
        return p(x)
    else:
        for i in range(x+1):    
            for j in range(i):
                print("*",end=" ")
            print()
p(n)
# Please write your code here.