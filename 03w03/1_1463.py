num = int(input())
count = 0

while num!= 1:
    if num %3 == 0 :
        num = num//3
        count = count +1 
        continue
    elif num %2 ==0 :
        num = num//2
        count = count +1 
        continue
    else : 
        num = num -1
        count = count +1 
        
print(count)