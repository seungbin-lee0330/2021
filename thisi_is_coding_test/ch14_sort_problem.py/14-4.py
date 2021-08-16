# import heapq

# n = int(input())

# heap = []
# for i in range(n):
    
#     data = int(input())
#     heapq.heappush(heap,data)
    
# result = 0

# while len(heap) != 1:
    
#     one = heapq.heappop(heap)
#     two = heapq.heappop(heap)
    
#     sum_value = one + two
#     result += sum_value
#     heapq.heappush(heap,sum_value)
    
# print(result)



#heap 구조 공부 항상 최소 힙이다
# 최대힙 구현하기

import heapq 

def heapsort(iterable):
    
    h = []
    result = []
    for value in iterable:
        heapq.heappush(h,-value)
    
    for i in range(len(h)):
        result.append(-heapq.heappop(h))
    
    return result

result = heapsort([1,7,3])
print(result)











# 잘못된 풀이
# 자료구조 힙을 써야하는 이유 - > 20 20 30 30 인 경우 20 + 20 = 40 으로 다음 연산시 30 + 30 을 먼저하는것이 유리하다

# n = int(input())    
# card_set =[]

# for i in range(n):
    
#     card_set.append(int(input()))
    
# card_set.sort()
# total_count = card_set[0] + card_set[1]

# for i in range(2,n):
    
#     total_count += (total_count + card_set[i])
    
# print(total_count)