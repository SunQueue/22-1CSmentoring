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

def promising(dArrValue, vArrValue):
    if dArrValue != 0 and vArrValue != 1 : #dataValue not 0 and not visited one
        return True
    else : return False
    
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
    if i >= 0 and j >= 0  and i < N and j < N:
        if promising(dataArr[i][j], visitArr[i][j]) :
            visitArr[i][j] = 1 #visited
            count+=1
            chk(i, j)
        else:
            visitArr[i][j] = 1
    else :
        return None
            
def chk(x, y):
    #try: 
        dfs(x-1, y)# U
        dfs(x+1, y)# D
        dfs(x, y-1)# L
        dfs(x, y+1)# R
    #except :
    #    print("ExceptionOccur")
    
search()

print(len(ans))
for k in range(0,len(ans)):
    print(ans[k])
