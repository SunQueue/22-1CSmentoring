import sys
#input = sys.stdin.readline을 아예 덮어버리기

N, K = map(int, input().split())

value = []
count = 0

for i in range(N):
    value.append(int(input()))
    
tmp = K
for j in range(N) :
    count += (tmp // value[N-j-1])
    tmp %= value[N-j-1]
    if tmp < 4 :
        count += tmp
        break

print(count)