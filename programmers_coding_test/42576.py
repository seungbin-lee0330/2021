from collections import Counter

def solution(participant, completion): # counter 사용
    answer = Counter(participant) - Counter(completion) # 카운터객체는 뺄셈이 가능하다
    print(answer.keys())
    return list(answer.keys())[0]
