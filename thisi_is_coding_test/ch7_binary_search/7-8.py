# n,m이 몹시 크다 따라서 이진 탐색을 써야한다 좋은문제다
# parametric search유형의 문제는 최적화문제를 결정문제로 바꾸어 해결하는 기법이다.
# 원하는 조건을 만족하는 가장 알맞은 값을 찾는 문제


n,m = list(map(int,input().split()))
array = list(map(int, input().split()))
start = 0
end = max(array)
result = 0

while start<=end:
    mid = (start+end) // 2
    total = 0 # sum은 함수가 있으므로 total을 쓰도록 하자
    for i in array:
        if i >= mid:
            total += i - mid
    if total < m:
        end = mid - 1
    else:
        result = mid
        start = mid + 1 # start <= end 될때 까지 반복하면서 mid값을 result로 넣는다

print(result)
        


















# 잘못된 풀이... 시간초과 날것이다
# n,m = list(map(int,input().split()))
# array = list(map(int, input().split()))
# height = max(array) - 1

# while True:
#     sum = 0
#     for i in array:
#         if i > height:
#             sum += (i - height)
#     if sum >= m:
#         break
#     height -= 1
    
# print(height)
        



















# n,m = list(map(int,input().split()))

# array = list(map(int, input().split()))

# start = 0
# end = max(array)

# result = 0

# while(start <= end):
#     total = 0
#     mid = (start + end) // 2
    
#     for x in array:
        
#         if x > mid:
#             total += x - mid
            
#     if total < m:
#         end = mid - 1
        
#     else:
#         result = mid
#         start = mid + 1
        
# print(result)