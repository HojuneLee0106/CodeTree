N = int(input())
moves = [tuple(map(int, input().split())) for _ in range(N)]
a, b = zip(*moves)
a, b = list(a), list(b)
pos=[]
ans_1=0
ans_2=0
f=[]
s=[]
for i in range(N):
    if a[i]==b[i]:
        continue
    else:
        if (a[i]==1 and b[i]==2) or (a[i]==2 and b[i]==3) or (a[i]==3 and b[i]==1):
            ans_1+=1

        elif (a[i] == 1 and b[i] == 3) or (a[i] == 3 and b[i] == 2) or (a[i] == 2 and b[i] == 1):
           ans_2 += 1

print(max(ans_2, ans_1))
# Please write your code here.