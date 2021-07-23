# for문을 쓰지 않는 방법을 생각






























# n,m,k = map(int,input().split())

# array = list(map(int,input().split()))

# array.sort()

# first = array[-1]
# second = array[-2]

# result = 0

# count = m // (k+1) * k
# count += m % (k+1) # 나머지도 더해줘야 함을 잊지 말자


# result += count * first
# result += (m-count) * second

# print(result)























# n,m,k = map(int,input().split())

# array = list(map(int,input().split()))

# array.sort()

# first = array[-1]
# second = array[-2]

# result = 0

# while True:
    
#     for i in range(k):
        
#         if m == 0:
#             break
        
#         result += first
#         m -= 1
        
#     if m == 0:
#         break
#     result += second
    
# print(result)
    

































# for i in range(m):  # 이렇게 짜도 가능할듯!!
    
#     if (i + 1) % k == 0:
#         result += second
        
#     else:
#         result += first
        
# print(result)











# n,m,k = map(int,input().split())
# data = list(map(int,input().split()))

# data.sort()
# first = data[n-1]
# second = data[n-2]

# count = int(m / (k+1)) *k  # 반복되는 수열로 나눈 몫에 k를 곱한만큼 더해진다
# count += m % (k+1) # 나머지가 있으면 더해준다

# result = 0
# result += count * first
# result += (m-count) * second

# print(result)   