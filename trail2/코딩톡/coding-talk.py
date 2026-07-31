n, m, p = map(int, input().split())
messages = [tuple(input().split()) for _ in range(m)]
c = [msg[0] for msg in messages]
u = [int(msg[1]) for msg in messages]
pos=[chr(i) for i in range(65,65+n)]
read=[]
if u[p-1]==0:
    print("")
else:
    start_idx=p-1
    for i in range(p-1):
        if u[i]==u[p-1]:
            start_idx=i
            break
    for i in range(start_idx, m):
        if c[i] in read:
            continue
        else:
            read.append(c[i])
    for j in range(len(pos)):
        if pos[j] in read:
            continue
        else:
            print(pos[j], end=" ")
# Please write your code here.