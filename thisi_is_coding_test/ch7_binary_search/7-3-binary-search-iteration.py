def binary_search(array,target,start,end):
    while start <= end: # 반복을 얼마나 할지 모르므로 while 조건으로 하는거지
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
            
    return None

n,target = map(int,input().split())
array = list(map(int,input().split()))
result = binary_search(array,target,0,n-1)

if result == None:
    print("원소가 존재하지 않습니다.")
else:
    print(result + 1)





















# def binary_search(array, target, start, end): # 반복문사용한 이진탐색
#     while start <= end:
#         mid = (start + end) // 2
        
#         if array[mid] == target:
#             return mid
    
#         elif array[mid] > target:
#             end = mid - 1
            
#         else:
#             start = mid + 1
            
#     return None

# n, target = map(int,input().split())

# array = list(map(int,input().split()))

# result = binary_search(array,target,0,n-1)

# if result == None:
#     print("원소가 존재하지 않습니다.")
    
# else: 
#     print(result + 1)
