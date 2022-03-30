#https://blog.naver.com/PostView.nhn?blogId=vjhh0712v&logNo=221470862600
import sys

N = int(input())

arr = [1, 2, 4]
for i in range(3,12) :
    arr.append(arr[i-3]+arr[i-2]+arr[i-1])
    
asked = []
for _ in range(0,N) :
    asked.append(int(input()))

for j in asked :
    print(arr[j-1])