# 다시풀기




























# n,k = map(int,input().split())         # 통과는 될듯 하나 문제에서 요구한 그대로가 아니다
# count = 0


# while n != 1:
    
#     if n % k == 0:    
#         n //= k
#         count += 1
        
#     else:
#         n -= 1
#         count += 1

# print(count)










# n,k = map(int,input().split())

# result = 0

# while n != 1:  
    
#     while n % k != 0:  # n이 k로 나누어 떨어지지 않으면 계속 빼줘야한다
#         n -= 1
#         result += 1
        
#     n //= k
#     result += 1
    
# print(result)



