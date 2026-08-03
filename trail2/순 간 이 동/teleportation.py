a, b, x, y = map(int, input().split())
curr=a
c=0
answer=[abs(b-a),abs(x-a)+abs(b-y), abs(y-a)+abs(b-x)]
print(min(answer))
# Please write your code here.