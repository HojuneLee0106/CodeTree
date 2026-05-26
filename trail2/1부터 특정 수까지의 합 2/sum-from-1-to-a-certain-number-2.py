N = int(input())
answer=0
def hap(x):
    global answer
    if x==1:
        return answer+1
    answer+=x
    return hap(x-1)
print(hap(N))
# Please write your code here.