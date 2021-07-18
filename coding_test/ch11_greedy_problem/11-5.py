# 다시풀어보기



























# 시간복잡도를 줄인 효율적인 풀이

n,m = map(int,input().split())
data = list(map(int,input().split()))

array = [0] * 11 # 1부터 10까지의 무게를 담을 수 있는 리스트 , 인덱스 맞춰주려고 11개 만든거

for x in data:
    
    array[x] += 1
    
result = 0

for i in range(1,m+1):
    
    n -= array[i]
    result += array[i] * n
    
print(result)











# 내 풀이 시간복잡도 괘 높다...

# n,m = map(int,input().split())

# weight = list(map(int,input().split()))

# count = 0

# for i in range(n):
#     for j in range(1,n-i):
    
#         if weight[i] != weight[i+j]:
#             count += 1
            
# print(count)