n = int(input())
name = []
street_address = []
region = []

for _ in range(n):
    n_i, s_i, r_i = input().split()
    name.append(n_i)
    street_address.append(s_i)
    region.append(r_i)
class person:
    def __init__(self,name, address, region):
        self.name=name
        self.address=address
        self.region=region
people=[]
for i in range(n):
    p=person(name[i], street_address[i],region[i])
    people.append(p)
people.sort(key=lambda x:x.name,reverse=True)
print("name",people[0].name)
print("addr",people[0].address)
print("city",people[0].region)
# Please write your code here.
