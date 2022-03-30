import sys

input = sys.stdin.readline
# input N & def 2D arr
N = int(input())
if N < 5 or N > 25 :
    raise Exception('customException: invalidInput')
print(N)

dataArr = []
visitArr = [[0]*N for _ in range(N)] # 0=not visited, 1=visited
ans = []
for i in range (N):
    dataArr.append(list(map(int, input().strip())))
    
count = 0

def search():
    global count
    i=0; j=0
    for i in range(N):
        for j in range(N):
            if visitArr[i][j] == 0  :# notVisited
                dfs(i, j)
                if count>0 : ans.append(count)
                count = 0

def dfs(i, j) :
    global count
    if i-1 >= 0 and j >= 0  and i-1 < N and j < N: #U
        if dataArr[i-1][j] != 0 and visitArr[i-1][j] != 1 : #if U promising
            visitArr[i-1][j] = 1 #visited
            count+=1
            dfs(i-1, j)
        else :
            visitArr[i-1][j] = 1
            
    if i+1 >= 0 and j >= 0  and i+1 < N and j < N: #D
        if dataArr[i+1][j] != 0 and visitArr[i+1][j] != 1 : #if D promising
            visitArr[i+1][j] = 1 #visited
            count+=1
            dfs(i+1, j)
        else :
            visitArr[i+1][j] = 1
            
    if i >= 0 and j-1 >= 0  and i < N and j-1 < N: #L
        if dataArr[i][j-1] != 0 and visitArr[i][j-1] != 1 : #if L promising
            visitArr[i][j-1] = 1 #visited
            count+=1
            dfs(i, j-1)
        else :
            visitArr[i][j-1] = 1
            
    if i >= 0 and j+1 >= 0  and i < N and j+1 < N: #R
        if dataArr[i][j+1] != 0 and visitArr[i][j+1] != 1 : #if R promising
            visitArr[i][j+1] = 1 #visited
            count+=1
            dfs(i, j+1)
        else:
            visitArr[i][j+1] = 1
    
search()

print(len(ans))
ans.sort()
for k in range(0,len(ans)):
    print(ans[k])
