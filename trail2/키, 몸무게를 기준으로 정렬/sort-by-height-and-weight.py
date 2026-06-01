n = int(input())
name = []
height = []
weight = []
for _ in range(n):
    n_i, h_i, w_i = input().split()
    name.append(n_i)
    height.append(int(h_i))
    weight.append(int(w_i))
class Profile:
    def __init__(self, name, height, weight):
        self.name=name
        self.height=height
        self.weight=weight
pro=[]
for i in range(n):
    x=Profile(name[i], height[i], weight[i])
    pro.append(x)
pro.sort(key=lambda x:(x.height,-x.weight))
for i in range(n):
    print(pro[i].name, pro[i].height, pro[i].weight)
# Please write your code here.