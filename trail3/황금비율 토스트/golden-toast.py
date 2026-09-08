n, m = map(int, input().split())
s = input()

commands = []
for _ in range(m):
    cmd = input().split()
    if len(cmd) == 1:
        commands.append((cmd[0],))
    else:
        commands.append((cmd[0], cmd[1]))
arr=list(s[i] for i in range(len(s)))
left_stack = list(s)
right_stack = []

for cmd in commands:
    if cmd[0] == 'L':
        if left_stack:
            right_stack.append(left_stack.pop())
            
    elif cmd[0] == 'R':
        if right_stack:
            left_stack.append(right_stack.pop())
            
    elif cmd[0] == 'P':
        left_stack.append(cmd[1])
        
    else: 
        if right_stack:
            right_stack.pop()
print("".join(left_stack + right_stack[::-1]))
# Please write your code here.
