n = int(input())
sequence = list(map(int, input().split()))
class num:
    def __init__(self,number,seq):
        self.number=number
        self.seq=seq
order_1=[]
order_2=[]
for i in range(n):
    x=num(sequence[i],i+1)
    order_1.append(x)
    order_2.append(x)
order_1.sort(key=lambda x:(x.number, x.seq))
answer=[]
for i in range(n):
    for j in range(n):
        if order_2[i].number==order_1[j].number and order_2[i].seq==order_1[j].seq:
            answer.append(j+1)
            break
print(*answer)

        # Please write your code here.
