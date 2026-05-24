n, m = map(int, input().split())
arr = list(map(int, input().split()))
queries = [tuple(map(int, input().split())) for _ in range(m)]

def hap(x,y):
    global arr
    sum=0
    for i in range(x-1,y):
        sum+=arr[i]
    return sum
for i in range(m):
    a,b=queries[i]
    print(hap(a,b))