N, K, P, T = map(int, input().split())
handshakes = [tuple(map(int, input().split())) for _ in range(T)]
handshakes.sort(key=lambda x:x[0])
c=[0 for _ in range(N+1)]
infec=[0 for _ in range(N+1)]
infec[P]=1
for i in range(T):
    if infec[handshakes[i][1]]==1:
        if c[handshakes[i][1]]>=K:
            if infec[handshakes[i][2]]==1:
                c[handshakes[i][2]]+=1
            c[handshakes[i][1]]+=1
        else:
            c[handshakes[i][1]]+=1
            if infec[handshakes[i][2]]==1:
                c[handshakes[i][2]]+=1
            infec[handshakes[i][2]]=1
    elif infec[handshakes[i][2]]==1:
        if c[handshakes[i][2]]>=K:
            if infec[handshakes[i][1]]==1:
                c[handshakes[i][1]]+=1
            c[handshakes[i][2]]+=1
        else:
            c[handshakes[i][2]]+=1
            if infec[handshakes[i][1]]==1:
                c[handshakes[i][1]]+=1
            infec[handshakes[i][1]]=1
for i in range(1,len(infec)):
    print(infec[i],end="")
# Please write your code here.