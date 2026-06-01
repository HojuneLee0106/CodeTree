n = 5
name = []
height = []
weight = []

for _ in range(n):
    n, h, w = input().split()
    name.append(n)
    height.append(int(h))
    weight.append(float(w))

class Profile:
    def __init__(self, name, height, weight):
        self.name=name
        self.height=height
        self.weight=weight
pro=[]
for i in range(5):
    x=Profile(name[i], height[i], weight[i])
    pro.append(x)
pro.sort(key=lambda x:x.name)
print("name")
for i in range(5):
    print(pro[i].name, pro[i].height, pro[i].weight)
print()
print("height")
pro.sort(key=lambda x:-x.height)
for i in range(5):
    print(pro[i].name, pro[i].height, pro[i].weight)
# Please write your code here.