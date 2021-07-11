# f = open("7-7.txt")
# input = f.readline

n = int(input())

array = set(map(int,input().split()))

m = int(input())

request = list(map(int, input().split()))

for i in request:
    
    if i in array:
        print('yes' , end = ' ')
        
    else:
        print('no', end = ' ')
        
    