N = int(input())
answer=0
def div(x):
    global answer
    if x==1:
        return answer
    else:
        answer+=1
        if x%2==0:
            return div(x//2)
        else:
            return div(x//3)
print(div(N)) 
# Please write your code here.