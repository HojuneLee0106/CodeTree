n = int(input())
arr = list(map(int, input().split()))

answer=[]
for i in range(n):
    new_arr=arr[:]
    new_arr[i]*=2
    for j in range(n):
        new=[]
        for k in range(n):
            if j==k:
                continue
            new.append(new_arr[k])
        su=0
        for k in range(len(new)-1):
            su+=abs(new[k]-new[k+1])
        answer.append(su)
print(min(answer))



# Please write your code here.