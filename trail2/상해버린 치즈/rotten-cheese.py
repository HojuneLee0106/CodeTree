N, M, D, S = map(int, input().split())

p, m, t = [], [], []
for _ in range(D):
    person, milk, time = map(int, input().split())
    p.append(person)
    m.append(milk)
    t.append(time)

sick_p, sick_t = [], []
for _ in range(S):
    person, time = map(int, input().split())
    sick_p.append(person)
    sick_t.append(time)
rotten={}
for i in range(S):
    sick=sick_p[i]
    for j in range(D):
        if p[j]==sick and t[j]<sick_t[i]:
            if m[j] not in rotten:
                rotten[m[j]] = set()
            rotten[m[j]].add(sick)
answer=0
for cheese in rotten:
    if len(rotten[cheese]) == S:
        current_cheese_people = set()
        for i in range(D):
            if m[i] == cheese:
                current_cheese_people.add(p[i])
        if len(current_cheese_people) > answer:
            answer = len(current_cheese_people)
print(answer)

# Please write your code here.