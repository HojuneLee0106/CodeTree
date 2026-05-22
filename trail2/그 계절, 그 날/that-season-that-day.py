Y, M, D = map(int, input().split())
weather={3:"Spring",4:"Spring",5:"Spring",6:"Summer",7:"Summer",8:"Summer",9:"Fall",10:"Fall",11:"Fall",1:"Winter",2:"Winter",12:"Winter"}
Month={1:True,3:True,4:False,5:True,6:False,7:True,8:True,9:False,10:True,11:False,12:True}
def yoon(x):
    if x%4==0:
        if x%100==0:
            if x%400==0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def real(y,m,d):
    if yoon(y):
        if m==2:
            if d<=29:
                return 1
            else:
                return -1
        elif m in Month:
            if Month[m]:
                if d<=31:
                    return 1
                else:
                    return -1
            else:
                if d<=30:
                    return 1
                else:
                    return -1
        else:
            return -1
    else:
        if m==2:
            if d<=28:
                return 1
            else:
                return -1
        elif m in Month:
            if Month[m]:
                if d<=31:
                    return 1
                else:
                    return -1
            else:
                if d<=30:
                    return 1
                else:
                    return -1
        else:
            return -1
if real(Y,M,D)==1:
    print(weather[M])
else:
    print(-1)
# Please write your code here.