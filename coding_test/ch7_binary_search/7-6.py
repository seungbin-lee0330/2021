n = int(input())
array = [0] * 100001

for i in input().split():
    array[int(i)] = 1
    
m = int(input())

request = list(map(int.input().split()))

for i in request:
    if array[i] == 1:
        print('yes', end = ' ')
        
    else: 
        print('no', end = ' ')