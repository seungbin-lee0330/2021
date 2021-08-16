stack = [] # FILO, LIFO 선입 후출, 후입 선출 구조로 먼저 들어간 데이터가 나중에 나온다

stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
stack.pop()
stack.append(1)
stack.append(4)
stack.pop()

print(stack)
print(stack[::-1]) # a와 b가 none 이므로 시작부터 끝까지 -1 이므로 역순으로 최상단 원소부터 출력
# 리스트 순서를 바꾸는방법 reverse와는 다르다!!!!!!!!!!!!!