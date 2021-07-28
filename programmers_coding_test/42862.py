def solution(n, lost, reserve):       
    
    answer = 0
    
    lost_cp = lost.copy() # copy를 쓰는것이 중요했다... lost_cp = lost 와는 완전 다르다
    
    for i in lost:
        if i in reserve:
            lost_cp.remove(i)
            reserve.remove(i)
    answer += (n - len(lost_cp))
    print(answer)
    lost_cp.sort()

    for i in lost_cp:  

        if (i - 1) in reserve:
            reserve.remove(i - 1)
            answer += 1

        elif (i + 1) in reserve:
            reserve.remove(i + 1)
            answer += 1
        print(answer)
    return answer


def solution(n, lost, reserve):       # copy를 쓰지 않는 방법
    
    answer = 0
    
    for i in range(1,n+1):
        if i in lost and i in reserve:
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
        print(answer)
    return answer