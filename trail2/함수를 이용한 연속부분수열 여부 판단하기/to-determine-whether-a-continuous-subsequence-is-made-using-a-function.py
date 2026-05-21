n1, n2 = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
answer="No"
for i in range(len(a)-len(b)+1):
    if a[i]==b[0]:
        k=0
        match=True
        for j in range(i,i+len(b)):
            if a[j]!=b[k]:
                match=False
                break
            else:
                k+=1
        if match:
            answer="Yes"
print(answer)
# Please write your code here.