user2_id, user2_level = input().split()
user2_level = int(user2_level)
class profile:
    def __init__(self, id="codetree", level=10):
        self.id=id
        self.level=level
user_1=profile()
user_2=profile(user2_id,user2_level)
print("user",user_1.id, "lv", user_1.level)
print("user",user_2.id, "lv", user_2.level)
# Please write your code here.
