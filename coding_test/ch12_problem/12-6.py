def possible(answer):
    
    for x,y,stuff in answer:
        
        if stuff == 0: # 기둥인 경우
            
            if y == 0 or [x-1,y,1] in answer or [x,y,1] in answer or [x,y-1,0] in answer:
                continue
            
            return False
        
        elif stuff == 1: # 보인 경우
            
            if [x,y-1,0] in answer or [x+1,y-1,0] in answer or ( [x-1,y,1] in answer and [x+1,y,1] in answer ):
                continue
                
            return False
    
    return True # for 문이 정상적으로 다 끝나면 즉 가능한 구조물이면 True를 반환해준다.

def solution(n,build_frame):
    
    answer = []
    for frame in build_frame:
        x,y,stuff,operate = frame
        
        if operate == 0:
            
            answer.remove([x,y,stuff])
            if not possible(answer):
                answer.append([x,y,stuff])
                
        elif operate == 1:
            
            answer.append([x,y,stuff])
            if not possible(answer):
                answer.remove([x,y,stuff])
                
    return sorted(answer)

        