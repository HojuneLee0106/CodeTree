n, m = map(int, input().split())
arr = list(map(int, input().split()))
wifi=[]
current=0
while True:
    if current>=n:
        break
    if arr[current]==1:
        current+=2*m+1
        wifi.append(current)
    else:
        current+=1
print(len(wifi))
# Please write your code here.