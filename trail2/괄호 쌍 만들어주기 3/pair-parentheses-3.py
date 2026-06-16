A = input()
answer=0
for i in range(len(A)):
    if A[i]=="(":
        for j in range(i,len(A)):
            if A[j]==")":
                answer+=1
print(answer)
# Please write your code here.