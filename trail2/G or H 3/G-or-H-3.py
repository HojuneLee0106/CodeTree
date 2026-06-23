import sys
input = sys.stdin.readline

n, k = map(int, input().split())
people = []
for _ in range(n):
    pos, char = input().split()
    score = 1 if char == "G" else 2
    people.append((int(pos), score))

people.sort()

answer = 0
total = 0
left = 0
for right in range(n):
    total += people[right][1]
    while people[right][0] - people[left][0] > k:
        total -= people[left][1]
        left += 1
    answer = max(answer, total)

print(answer)