def binary_search(array,target,start,end): # logN의 시간복잡도를 가진다 굳굳
    if start > end:
        return None
    mid = (start + end) // 2   
    if array[mid] == target:
        return mid   
    elif array[mid] > target:
        return binary_search(array,target,start,mid-1) # return을 해주어야 함을 잘 생각하자        
    else:
        return binary_search(array,target,mid+1,end)
        
n,target = map(int,input().split())
array = list(map(int,input().split()))
result = binary_search(array,target,0,n-1)

if result == None:
    print("원소가 존재하지 않습니다.")
else:
    print(result + 1)





















# def binary_search(array,target,start,end): # 재귀함수 사용방법
#     if start > end:
#         return None
#     mid = (start + end) // 2 # 소수점은 버리고 작은값을 중간점으로 취한다
    
#     if array[mid] == target:
#         return mid
    
#     elif array[mid] > target:
#         return binary_search(array, target, start, mid-1)
    
#     else:
#         return binary_search(array,target,mid + 1, end)
    
# n, target = map(int,input().split()) # 기본적으로 input은 string 문자열이므로 int로 형변환 해준다

# array = list(map(int,input().split()))

# result = binary_search(array,target,0,n-1)

# if result == None:
#     print("원소가 존재하지 않습니다.")
    
# else:
#     print(result + 1) # index + 1 을 출력해서 몇번째인지를 알려준다.
    