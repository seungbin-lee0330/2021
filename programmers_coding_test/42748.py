def solution(array, commands):
    answer = []
    
    for command in commands:
        i,j,k = command # 배열에 있는 값들 한번에 받아오기
        answer.append(sorted(array[i-1:j])[k-1])
    
    return answer