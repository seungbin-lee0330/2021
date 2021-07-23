def solution(n, lost, reserve):       
    
    answer = 0
    for i in lost:
        if i in reserve:
            lost.remove(i)
            reserve.remove(i)
    answer += (n - len(lost))
    
    
    lost.sort()
    
    for i in lost:  
            
        if (i - 1) in reserve:
            reserve.remove(i - 1)
            answer += 1
            
        elif (i + 1) in reserve:
            reserve.remove(i + 1)
            answer += 1
            
    return answer


def solution(n, lost, reserve):       
    
    answer = 0
    lost.sort()
    
    for i in lost:  
        
        if i in reserve:
            lost.remove(i)
            reserve.remove(i)
            
        elif (i - 1) in reserve:
            reserve.remove(i - 1)
            answer += 1
            
        elif (i + 1) in reserve:
            reserve.remove(i + 1)
            answer += 1
            
    answer += (n - len(lost))
    return answer