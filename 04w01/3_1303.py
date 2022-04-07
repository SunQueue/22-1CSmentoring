from collections import deque
import sys

input = sys.stdin.readline

N, M = map(int, input().split())

arr = []
visited = [[False]*N for _ in range(M)]
deq = deque()

bWeight = 0
wWeight = 0

for i in range(M):
    arr.append(list(input().strip()))
    
# dfs(x,y)

def dfs(initX, initY):
    tmpWeight = 0
    
    deq.append((initX, initY))
    
    while deq:
        x, y = deq.pop()
        cmpChar = arr[x][y]
        for xw, yw in [(-1, 0), (1, 0), (0, -1), (0, 1)]: #Search U D L R
            if 0<= xw <= N and 0<= yw <= M :
                deq.append((xw, yw))
                if arr[xw][yw] is cmpChar :
                    visited[xw][yw] = True
                    tmpWeight +=1
        
dfs(0,0)

        
#   상하좌우 탐색
#   deq.append()상, 하, 좌, 우
#   if 상하좌우가 범위 내일 경우
#   
#       promising
#       1. bound 이내면서,  2. cmpChar과 동일하면
#           visited[newNode]
#           tmpWeight++
#   탐색 끝
#   해당문자Weight += tmpWeight**2
    # if new node char is equal cmpChar)