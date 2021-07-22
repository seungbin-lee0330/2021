from collections import deque # que는 라이브러리에서 불러와야 한다

queue = deque() # FIFO 선입선출 구조 , 나중에 들어오면 나중에 나간다

queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft() # .popleft() 쓰는것에 주의할 것
queue.append(1)
queue.append(4)
queue.popleft()

print(queue)
queue.reverse()
print(queue)

# 리스트 형태로 바꾸고 싶다면 list(queue) 쓰면 끝
