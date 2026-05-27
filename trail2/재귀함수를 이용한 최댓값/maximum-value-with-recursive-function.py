n = int(input())
arr = list(map(int, input().split()))
answer=0
def big(x):
    global answer
    if x==1:
        if arr[x-1]>answer:
            answer=arr[x-1]
            return answer
        else:
            return answer
    else:
        if arr[x-1]>answer:
            answer=arr[x-1]
            return big(x-1)
        else:
            return big(x-1)
print(big(n))
# Please write your code here.