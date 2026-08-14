n = int(input())
a = list(map(int, input().split()))
new_a=a[:]
new_a.sort()
s=list(set(new_a))
pos=True
c=0
answer=0
if len(s)==1:
    pos=False
else:
    target=s[1]
if pos:
    for i in range(n):
        if a[i]==target:
            c+=1
            answer=i+1
if c==1:
    print(answer)
else:
    print(-1)
# Please write your code here.