dirs = input()
curr=0
x=0
y=0
for i in range(len(dirs)):
    if dirs[i]=="F":
        if curr==0:
            y+=1
        elif curr==1:
            x+=1
        elif curr==2:
            y-=1
        else:
            x-=1
    elif dirs[i]=="L":
        curr-=1
        curr%=4
    else:
        curr+=1
        curr%=4
print(x,y)
# Please write your code here.