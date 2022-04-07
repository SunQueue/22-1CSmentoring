import sys
from collections import deque

UPPER_LIMIT = 100001

input = sys.stdin.readline

st, dest = map(int, input().split())
deq = deque()

boundCount = 0
rep = 0

#dfs
deq.append(st)

while deq :
    x = deq.popleft()
    if rep == 0 and len(deq) > 3 ** boundCount :
        boundCount += 1
    if rep >= 0 and len(deq) > 3 ** boundCount :
        break;
    if x+1  > UPPER_LIMIT :
        if x*2 > UPPER_LIMIT :
            if x-1 > UPPER_LIMIT :
                break;
    
    if x -1 == dest or x +1 == dest or x *2 == dest :
        rep +=1
    else :
        deq.append(x-1)
        deq.append(x+1)
        deq.append(x*2)  

print(boundCount)
print(rep)