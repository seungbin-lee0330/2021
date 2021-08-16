# 어려움 다시 봐야할듯

























# from itertools import permutations

# def solution(n, weak, dist): # n,weak 매우 작다 - > 완전탐색
    
#     length = len(weak)
#     for i in range(length):
#         weak.append(weak[i] + n) # 길이를 2배로 늘려서 원형을 일자형태로 변형
        
#     answer = len(dist) + 1
    
#     for start in range(length): # 시작점 각각 설정
        
#         for friends in list(permutations(dist,len(dist))): # 친구를 나열하는 모든 경우의 수 각각에 대하여 확인
        
#             count = 1
            
#             position = weak[start] + friends[count - 1]
            
#             for index in range(start,start + length):
#                 if position < weak[index]:
#                     count += 1 # 새로운 친구를 투입
#                     if count > len(dist):
#                         break
#                     position = weak[index] + friends[count-1]
#             answer = min(answer,count)
        
#     if answer > len(dist):
#         return -1
    
    
#     return answer