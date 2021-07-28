# f = open("7-7.txt")
# input = f.readline

n = int(input())
store = set(map(int,input().split())) # set는 중괄호 {} 로 표현된다
m = int(input())
request = list(map(int, input().split()))

for i in request:
    if i in store:
        print('yes' , end = ' ')
    else:
        print('no', end = ' ')
        
 # f.close()   