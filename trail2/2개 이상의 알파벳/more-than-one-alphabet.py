A = input()
def check(S):
    check_list=[]
    for i in range(len(S)):
        if S[i] in check_list:
            continue
        else:
            check_list.append(S[i])
    return check_list
if len(check(A))>=2:
    print("Yes")
else:
    print("No")
# Please write your code here.