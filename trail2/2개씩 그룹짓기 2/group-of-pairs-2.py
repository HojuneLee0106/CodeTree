n = int(input())
arr = list(map(int, input().split()))
2, 5, 7, 9, 10, 15
arr.sort()
diff=[]
for i in range(2*n//2):
    d=(arr[i+2*n//2]-arr[i])
    diff.append(d)
answer=min(diff)
print(answer)
# Please write your code here.