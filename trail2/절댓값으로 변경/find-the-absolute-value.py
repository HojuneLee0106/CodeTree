n = int(input())
arr = list(map(int, input().split()))
def ab(L, N):
    for i in range(N):
        L[i]=abs(L[i])
    return L
print(*ab(arr,n))
# Please write your code here.