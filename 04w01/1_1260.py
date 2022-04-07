from collections import deque

node, edge, v_sp = list(map(int, input().split()))

#get arr

data = [[]*(node+1) for _ in range (edge+1)]
dvalid = [False] * (node+1)
bvalid = [False] * (node+1)

#dResult = [v_sp]
#bResult = [v_sp]

for _ in range (edge) :
    x, y = map(int, input().split())
    data[x].append(y)
    data[y].append(x)

#print(f"data = {data}")

def dfs(sp) :
    print(sp, end=' ')
    global dvalid
    if dvalid[sp] is False :
        dvalid[sp] = True
        for i in data[sp] :
            if dvalid[i] is False :
                #dResult.append(i)
                dfs(i)

def bfs(sp) :
    print(sp, end=' ')
    global bvalid
    if bvalid[sp] is False :
        bvalid[sp] = True
        for i in data[sp] :
            #bResult.append(i)
            bvalid[i] = True
        for j in data[sp]:
            bfs(j)

dfs(v_sp)
#print(dResult)
print()
bfs(v_sp)
#print(bResult)