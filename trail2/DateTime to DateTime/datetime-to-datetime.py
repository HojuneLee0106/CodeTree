a, b, c = map(int, input().split())
day=60*24
answer=0
target=day*(a-11)
target+=60*b
target+=c
standard=11*60+11
if target<standard:
    print(-1)
else:
    print(target-standard)

         
# Please write your code here.