binary = input()
answer=0
x=1
for i in range(len(binary)):
    if int(binary[len(binary)-1-i])==0:
        x*=2
        continue
    else:
        answer+=x
        x*=2
print(answer)