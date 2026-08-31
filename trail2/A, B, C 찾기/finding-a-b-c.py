arr = list(map(int, input().split()))
arr.sort()
A=arr[0]
B=arr[1]
S=arr[-1]
C=S-A-B
print(A, B, C)
# Please write your code here.