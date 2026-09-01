N = int(input())

command = []
num = []

for _ in range(N):
    line = input().split()
    command.append(line[0])
    if line[0] == "push_back" or line[0] == "get":
        num.append(int(line[1]))
    else:
        num.append(0)
answer=[]
for i in range(N):
    if command[i] == "push_back":
        answer.append(num[i]) 
    elif command[i] == "get":
        print(answer[num[i]-1])
    elif command[i] == "size":
        print(len(answer))
    else:
        answer.pop()
# Please write your code here.
