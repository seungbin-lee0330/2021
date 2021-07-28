# 다시풀기




















# def solution(N, stages): 
#     answer = []
#     players = len(stages)
    
#     for i in range(1,N+1):
        
#         if players == 0: # 분모가 0인 케이스를 고려해야한다는 점
#             fail_rate = 0
        
#         else:
#             fail_rate = stages.count(i) / players
#             players -= stages.count(i)
        
#         answer.append((i,fail_rate))
    
#     answer = sorted(answer,key=lambda x: x[1], reverse=True)
#     answer = [i[0] for i in answer]
        
#     return answer