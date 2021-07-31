def solution(answers): 
    
    one = [1,2,3,4,5] # 패턴은 나머지로 처리해버리기
    two = [2,1,2,3,2,4,2,5] 
    three = [3,3,1,1,2,2,4,4,5,5] 
    score = [0,0,0] # score를 리스트로 한번에 관리하자
    result = [] 
    
    for idx,answer in enumerate(answers): # enumerate로 index와 값 동시에 받기
        if answer == one[idx % len(one)]:
            score[0] += 1
        if answer == two[idx % len(two)]:
            score[1] += 1
        if answer == three[idx % len(three)]:
            score[2] += 1
    for idx,s in enumerate(score):
        if s == max(score):
            result.append(idx+1)
    return result