secret_code, meeting_point, time = input().split()
time = int(time)
class Meeting:
    def __init__(self, secret, place, time):
        self.secret=secret
        self.place=place
        self.t=time
M1=Meeting(secret_code, meeting_point, time)
print("secret code :",M1.secret)
print("meeting point :",M1.place)
print("time :",M1.t)
# Please write your code here.