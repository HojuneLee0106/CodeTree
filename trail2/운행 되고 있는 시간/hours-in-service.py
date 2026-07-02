n = int(input())
times = [tuple(map(int, input().split())) for _ in range(n)]
a = [t[0] for t in times]
b = [t[1] for t in times]
answer=[]
for i in range(n):
    hap=0
    arr=[0 for _ in range(max(b)+1)]
    for j in range(n):
        if i==j:
            continue
        else:
            for k in range(a[j],b[j]):
                arr[k]=1
    hap=sum(arr)
    answer.append(hap)
print(max(answer))

# Please write your code here.