n = int(input())
arr = list(map(int, input().split()))
count=0
for i in range(n):
    s=0
    for j in range(i,n):
        s+=arr[j]
        length=j-i+1
        for k in range(i,j+1):
            if arr[k]*length==s:
                count+=1
                break
print(count)
# Please write your code here.