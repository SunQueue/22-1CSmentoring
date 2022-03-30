target = int(input())

arr= [0, 1, 3]
for i in range (3,target+1) :
    arr.append(arr[i-2]*2 + arr[i-1])
    
print(arr[target]%10007)