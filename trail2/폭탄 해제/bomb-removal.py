unlock_code, wire_color, seconds = input().split()
seconds = int(seconds)
class solve:
    def __init__(self, unlock, wire, second):
        self.unlock=unlock
        self.wire=wire
        self.second=second
S1=solve(unlock_code, wire_color, seconds)
print("code :",S1.unlock)
print("color :",S1.wire)
print("second :",S1.second)
# Please write your code here.