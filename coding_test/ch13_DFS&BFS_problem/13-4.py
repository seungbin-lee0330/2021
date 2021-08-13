def balanced_index(p):
    count = 0
    for i in range(len(p)):
        if p[i] == '(':
            count += 1
        else:
            count -= 1
        if count == 0:
            return i
        
def check_proper(p): # 올바른 괄호 문자열인지 판단
    count = 0
    for i in p:
        if i == '(':
            count += 1    
        else:
            if count == 0:
                return False # 올바르지 않으면 False 리턴한다
            count -= 1
    return True 
        
def solution(p):
    answer = ''
    if p == '':
        return answer  
    index = balanced_index(p) 
    u = p[:index + 1] # '(',')' 의 개수가 맞는 첫번째 지점을 확인한다
    v = p[index + 1:]
    if check_proper(u):
        answer = u + solution(v)
    else:
        answer = '('
        answer += solution(v)
        answer += ')'
        u = list(u[1:-1]) # 첫번째와 마지막 문자를 제거
        for i in range(len(u)):
            if u[i] == '(':
                u[i] = ')'
            else:
                u[i] = '('
        answer += "".join(u)
    return answer