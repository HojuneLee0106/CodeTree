commands = input()
dx=[0,1,0,-1]
dy=[1,0,-1,0]
curr=0
x=0
y=0
mapper={"R":1,"L":-1}
time=0
pos=-1
for i in range(len(commands)):
    if commands[i]=="F":
        x+=dx[curr]
        y+=dy[curr]
        time+=1
    elif commands[i]=="L":
        curr+=mapper["L"]
        curr%=4
        time+=1
    else:
        curr+=mapper["R"]
        curr%=4
        time+=1
    if x==0 and y==0 and pos==-1:
        pos=time
        break
if pos!=-1:
    print(pos)
else:
    print(-1)
# Please write your code here.