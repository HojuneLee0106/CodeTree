n = int(input())
answer=0
def cal(x):
    global answer
    if x==1:
        return answer
    elif x%2==0:
        answer+=1
        return cal(x//2)
    else:
        answer+=1
        return cal(x*3+1) 
print(cal(n))
# Please write your code here.