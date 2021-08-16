# 어려운문제 다시 풀어보기

def solution(s):
    result = len(s)
    for step in range(1,len(s)//2 + 1): 
        # 몇개 단위로 압축할것인가 step으로 써야 가독성이 좋다
        compressed = ''
        iter = s[:step]
        count = 1
        for j in range(step,len(s),step):
            if s[j:j+step] == iter: # 이렇게 쓸경우 초과하지 않는다
                count += 1
            else:
                compressed += str(count) + iter if count >=2 else iter
                iter = s[j:j+step]
                count = 1
        compressed += str(count) + iter if count >=2 else iter
        result = min(result,len(compressed))
    return result























# def solution(s): # 완전탐색
#     answer = len(s)
#     for step in range(1,len(s)//2 + 1): # 반복주기를 1부터 전체길이의 절반까지 확인한다
#         compressed = ""
#         prev = s[0:step] # 처음부터 step 만큼의 문자열 추출
#         count = 1
#         for j in range(step,len(s),step):
#             if prev == s[j:j+step]:
#                 count += 1
#             else:
#                 compressed += str(count) + prev if count >= 2 else prev
#                 prev = s[j:j+step]
#                 count = 1
#         compressed += str(count) + prev if count >=2 else prev
#         answer = min(answer,len(compressed)) 
        
#     return answer