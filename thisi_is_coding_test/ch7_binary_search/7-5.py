def binary_search(array,target,start,end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None      















# n = int(input())
# store = list(map(int,input().split()))
# store.sort() # 이진 탐색을 하기 위해서는 반드시 정렬을 해주어야 한다!!!!!!!!!!!!!!
# m = int(input())
# request = list(map(int,input().split()))

# for i in request:
#     check = binary_search(store,i,0,n-1)
#     if check == None:
#         print("no", end =" ")
#     else:
#         print("yes", end = " ")



# n = int(input())

# array = list(map(int,input().split()))
# array.sort() # 이진 탐색하기 전에 정렬 수행

# m = int(input())

# request = list(map(int,input().split()))

# for i in request:
#     result = binary_search(array,i,0,n-1)

#     if result != None:
#         print('yes',end = ' ')
        
#     else:
#         print('no', end= ' ')