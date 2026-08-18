n = int(input())
blocks = [int(input()) for _ in range(n)]
h=sum(blocks)
m=h//n
answer=0
diff=0
for i in range(n):
    diff+=abs(blocks[i]-m)
print(diff//2)

    
        
# Please write your code here.