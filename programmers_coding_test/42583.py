# 입력받은 인자들을 최대한 잘 활용해서 새로운 문자를 최소화하자
def solution(bridge_length, weight, truck_weights):
    answer = 0 # 경과시간
    bridge = [0] * bridge_length # 전형적인 초기화 방법 도로를 시각화 함
    current_weight = 0
    while bridge:
        answer += 1 # 시간을 먼저 더하고 시작하는게 맞다
        current_weight -= bridge.pop(0) # 리스트를 큐처럼 쓰고싶을 때 자주쓴다
        if truck_weights: # 이걸 고려하는게 어렵다
            if current_weight + truck_weights[0] <= weight:
                current_weight += truck_weights[0]
                bridge.append(truck_weights.pop(0))
            else:
                bridge.append(0)
    return answer