inp = [input() for _ in range(3)]
answer=[]
for i in range(3):
    pos=[]
    for j in range(3):
        if inp[i][j] in pos:
            continue
        else:
            pos.append(inp[i][j])
    if len(pos)==2:
        if pos in answer:
            continue
        else:
            answer.append(pos)
for i in range(3):
    pos=[]
    for j in range(3):
        if inp[j][i] in pos:
            continue
        else:
            pos.append(inp[j][i])
    if len(pos)==2:
        if pos in answer:
            continue
        else:
            answer.append(pos)
pos=[]
for i in range(3):
    if inp[i][i] in pos:
        continue
    else:
        pos.append(inp[i][i])
if len(pos)==2:
    if pos not in answer:
        answer.append(pos)
pos=[]
for i in range(3):
    if inp[i][2-i] in pos:
        continue
    else:
        pos.append(inp[i][2-i])
if len(pos)==2:
    if pos not in answer:
        answer.append(pos)
print(len(answer))
# Please write your code here.