n = int(input())
def star(x):
    global n
    if x>n:
        return
    else:     
        for i in range(x):
            print("*",end="")
        print()
        return star(x+1)
star(1)
# Please write your code here.