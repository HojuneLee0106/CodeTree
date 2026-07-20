nums = list(map(int, input().split()))
nums.sort()
def solve():
    for a in range(1, 41):
        for b in range(a, 41):
            for c in range(b, 41):
                for d in range(c, 41):
                    temp = [
                        a, b, c, d,
                        a+b, a+c, a+d, b+c, b+d, c+d,
                        a+b+c, a+b+d, a+c+d, b+c+d,
                        a+b+c+d
                    ]
                    temp.sort()
                    if temp == nums:
                        print(a, b, c, d)
                        return

solve()
# Please write your code here.