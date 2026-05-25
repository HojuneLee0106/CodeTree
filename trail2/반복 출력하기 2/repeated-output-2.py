n = int(input())
def HW(x):
    if x==0:
        return 0
    print("HelloWorld")
    return HW(x-1)
HW(n)
# Please write your code here.