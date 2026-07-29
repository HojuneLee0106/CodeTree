N, L = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort(reverse=True)
answer=0
for H in range(N, 0,-1):
    min_val=arr[H-1]
    if min_val>=H:
        answer=H
        break
    
    elif min_val==H-1:
        c=0
        for j in range(H-1,-1,-1):
            if arr[j]==H-1:
                c+=1
            else:
                break
        if c<=L:
            answer=H
            break
print(answer)