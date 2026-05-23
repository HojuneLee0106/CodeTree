A = input()
def flip(C):
    for i in range(len(C)):
        if C[i]==C[len(C)-i-1]:
            continue
        else:
            return 0
            break
    return 1
if flip(A)==1:
    print("Yes")
else:
    print("No")
# Please write your code here.