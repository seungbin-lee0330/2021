# 어려운 문제 다시 풀어보기
























# import heapq

# def solution(food_times, k):

#     if sum(food_times) <= k:
#         return -1
    
#     q =[]
#     for i in range(len(food_times)):
#         heapq.heappush(q,(food_times[i],i+1)) #음식시간 음식번호
        
#     sum_value = 0 # 먹기위해 사용한 시간
#     previous = 0 # 직전에 다 먹은 음식시간
#     length = len(food_times)
    
#     while sum_value + ((q[0][0] - previous) * length) <= k:
#         now = heapq.heappop(q)[0]
#         sum_value += (now - previous) * length
#         length -= 1
#         previous = now
        
#     result = sorted(q,key = lambda x:x[1]) # lambda 는 익명함수이고 음식번호 기준으로 정렬하는 방법
#     return result[(k - sum_value) % length][1]












#내 풀이

def solution(food_times, k):
    answer = 0
    
    while True:
        i = 0
        for i in range(len(food_times)):
            if k == 0:
                answer = i + 1
                break
            
            if food_times[i] != 0:
                food_times[i] -= 1
                k -= 1
              
    return answer