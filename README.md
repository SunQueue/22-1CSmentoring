"# 22-1CSmentoring" 

# 03W03

### 15486
- import sys 쓰는것 권장 (input()하는 것보다); 입력 버퍼를 통해 받는 것을 권장.
- rstrip()과 split()차이: 전자는 character단위, 후자는 공백 기준으로 구분. 둘 다 개행 지우기 위해 사용

# 03W04
- strip(), split() 
- join(list) //붙이기
>> 용례; print('',join(list))

### 1012
- sys.setrecursionlimit() 필요

#### DFS/BFS 접근 tip
- arr초기화 방법
> arr = [[0]*n for _ in range(m)] #이거 그대로 쓰면 될 듯

- map(int, input().split())
> map(int, input().split()) 이랑 list(map(int, input().split()))) 차이점?

- 상하좌우 탐색이 필요한 경우 -> 배열을 만들어서 접근하는게 나을 것.
> 예) move = [상,하,좌,우]; ((1,0)의 형식으로.)

- dfs는 재귀로 구현하는 것이 맞지만, 시간문제상 deque를 쓰는 것을 권장.
>def dfs(x,y):
>   deq = deque() #deque선언 후
>   deq.append(---) #베추 위치 append
>
>   while deq: #deq에 뭐라도 있을 경우 return true; deq가 빌때까지 돌겠다. 
>       popY, popX = deq.pop()... #tuple형태로 선언했으니, 받는것도 그와같이
>           pop 한 값에 상하좌우 loop :
>               pop 한 값에 상하좌우 한 값이 범위 내에 있을 경우:
>                   작업.
> 
>popY, popX = deq.popleft()하는 경우 BFS형식으로 변형하여 구현이 가능
>
>pop()은 뒤에 들어온놈부터 터는데
>popleft()는 먼저 들어온놈부터 턺