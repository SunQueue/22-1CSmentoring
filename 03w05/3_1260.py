from collections import deque

N, M, v_sp = list(map(int, input().split()))

deq_dfs = deque()
deq_bfs = deque()
visited = [False]*(N+1)
dresult = []
bresult = []

for _ in range(M):
    node1, node2 = map(int, input().split())
    deq_dfs.append((node1, node2))
deq_bfs = deq_dfs.copy()
    

#deq_dfs.sort()
# while deq_dfs:
#     dnode1, dnode2= deq_dfs.pop()
    
#     if visited[dnode1] == False :
#         visited[dnode1] = True
#         dresult.append(int(dnode1))
#     if visited[dnode2] == False :
#         visited[dnode2] = True
#         dresult.append(int(dnode2))       
# print(dresult) 

    

#bfs
while deq_bfs:
    bnode1, bnode2= deq_bfs.popleft()
    
    if visited[bnode1] == False :
        visited[bnode1] = True
        bresult.append(int(bnode1))
    if visited[bnode2] == False :
        visited[bnode2] = True
        bresult.append(int(bnode2))       
print(bresult) 

