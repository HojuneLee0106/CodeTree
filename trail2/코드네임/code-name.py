MAX_N = 5

codenames = []
scores = []
for _ in range(MAX_N):
    codename, score = input().split()
    codenames.append(codename)
    scores.append(int(score))
class agent:
    def __init__(self, name, score):
        self.name=name
        self.score=score
agents=[]
for i in range(MAX_N):
    agents.append(agent(codenames[i],scores[i]))

agents.sort(key=lambda x:x.score)
print(agents[0].name,agents[0].score)
# Please write your code here.
