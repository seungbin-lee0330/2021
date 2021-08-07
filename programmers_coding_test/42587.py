# 모르겠다 시간 엄청 오래걸림
from collections import deque
def solution(priorities, location):
    answer = 0
    q = deque([(v,i) for i,v in enumerate(priorities)]) 
    # value와 index를 같이 저장하여 구분하기 위해 튜플형태로 큐를 구성함
    while len(q):
        item = q.popleft()
        if q and item[0] < max(q)[0]: 
            # 튜플의 첫번째 성분을 기준으로 max값이 결정된다
            q.append(item)
        else:
            answer += 1
            if item[1] == location:
                break
    return answer