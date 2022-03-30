#howto; 
dp = [[1]*10]
print(dp)

tmparr = [0]*10
for i in range(0, 10) :
    for j in range(0,10):
        tmparr[j] += dp[i][j]
    print(tmparr)