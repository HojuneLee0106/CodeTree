text = input()
pattern = input()
def check(x,y):
    val=-1
    for i in range(len(text)-len(pattern)+1):
        answer=[]
        if x[i]==y[0]:
            answer.append(i)
            for j in range(len(pattern)):
                val=False
                if x[i+j]!=y[j]:
                    val=False
                    break
                else:
                    val=True
            if val==True:
                return answer[0]
    return -1
print(check(text, pattern)) 
# Please write your code here.