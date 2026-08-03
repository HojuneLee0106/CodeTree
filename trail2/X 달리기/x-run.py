X = int(input())
distance=0
speed=1
time=0
while distance<X:
    distance+=speed
    time+=1
    remain=X-distance
    if remain>=(speed+1)*(speed+2)//2:
        speed+=1
    elif remain>=speed*(speed+1)//2:
        speed=speed
    else:
        speed-=1
print(time)
    
# Please write your code here.