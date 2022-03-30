#tokenize N
N = int(input())
numList = list(map(int, str(N)))
numList.sort(reverse=True)

ans = 0

#if 3배수 && '0' 1개 이상 : tokenized된 큰 수부터 앞에 정렬 -> int
if sum(numList) %3 == 0  and 0 in numList :
    for i in numList:# 굳이 이걸 돌 필요가 없음.
        ans *= 10
        ans += int(i)
    print(ans)
    
else : print(-1)