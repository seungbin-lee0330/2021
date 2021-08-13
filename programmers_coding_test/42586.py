def solution(progresses, speeds):  # 어려웠다
    print(progresses)
    print(speeds)
    answer = []
    time = 0
    count = 0
    while len(progresses)> 0:
        if (progresses[0] + time*speeds[0]) >= 100: # 재귀적으로 어디 들어가야할지 정하는게 중요
            progresses.pop(0)
            speeds.pop(0)
            count += 1
        else:
            if count > 0:
                answer.append(count)
                count = 0
            time += 1
    answer.append(count)
    return answer














# from collections import deque  # 너무 별로다.... n제곱 풀이...

# def solution(progresses, speeds):
#     answer = []
#     queue = deque()
#     queue2 = deque()
#     for i,j in zip(progresses,speeds):
#         queue.append(i)
#         queue2.append(j)
#     while len(queue) != 0:
#         count = 0
#         for i in range(len(queue)):
#             queue[i] += queue2[i]
#         while len(queue) != 0 and queue[0] >= 100:
#             queue.popleft()
#             queue2.popleft()
#             count += 1
#         if count >= 1:
#             answer.append(count)
#     return answer