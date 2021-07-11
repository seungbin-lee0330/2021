def binary_search(array,target,start,end):
    if start > end:
        return None
    mid = (start + end) // 2
    
    if array[mid] == target:
        return mid
    
    elif array[mid] > target:
        return binary_search(array, target, start, mid-1)
    
    else:
        return binary_search(array,target,mid + 1, end)
    
n, target = list(map(int,input().split())) # 왜 리스트로 받았을까

array = list(map(int,input().split()))

result = binary_search(array,target,0,n-1)

if result == None:
    print("원소가 존재하지 않습니다.")
    
else:
    print(result + 1) # index + 1 을 해서 몇번째인지를 알려준다.
    