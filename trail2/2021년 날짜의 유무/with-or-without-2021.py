M, D = map(int, input().split())
Month={1:True,3:True,4:False,5:True,6:False,7:True,8:True,9:False,10:True,11:False,12:True}
if M==2:
    if D<=28:
        print("Yes")
    else:
        print("No")
elif M in Month:
    if Month[M]:
        if D<=31:
            print("Yes")
        else:
            print("No")
    else:
        if D<=30:
            print("Yes")
        else:
            print("No")
else:
    print("No")
# Please write your code here.