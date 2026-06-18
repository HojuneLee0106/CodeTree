n = int(input())
numbers = list(map(int, input().split()))
answer=[]
for i in range(n-2):
    for j in range(i+2,n):
        answer.append(numbers[i]+numbers[j])
print(max(answer))
# Please write your code here.