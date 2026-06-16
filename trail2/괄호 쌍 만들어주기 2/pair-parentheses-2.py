A = input()
answer=0
for i in range(len(A)-1):
    if A[i]=="(":
        if A[i+1]=="(":
            for j in range(i+2,len(A)-1):
                if A[j]==")":
                    if A[j+1]==")":
                        answer+=1
print(answer)
# Please write your code here.