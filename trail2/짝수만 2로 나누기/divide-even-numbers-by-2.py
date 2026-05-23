n = int(input())
arr = list(map(int, input().split()))
def change(l, n):
    for i in range(len(l)):
        if l[i]%2==0:
            l[i]=l[i]//2
change(arr,n)
print(*arr)
# Please write your code here.