n = int(input())
arr = list(map(int, input().split()))
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def lcm(a, b):
    return a * b // gcd(a, b)

def lcm_all(idx):
    if idx == 0:
        return arr[0]
    return lcm(lcm_all(idx - 1), arr[idx])

print(lcm_all(n - 1))