



























# 평균적으로 시각복잡도 nlogn이지만 최악의 경우 n^2 이다
array = [5,7,9,0,3,1,6,2,4,8]

def quick_sort(array,start,end): # start는 시작 인덱스 end는 마지막 인덱스
    if start >= end: # 원소가 1개인 경우 종료
        return
    pivot = start
    left = start + 1
    right = end
    while  left <= right:
        while left <= end and array[left] <= array[pivot]: # 피벗보다 크지 않으면 계속 탐색
            left += 1
        while right > start and array[right] >= array[pivot]: # 피벗보다 작지 않으면 계속 탐색
            right -= 1
        if left > right: # 엇갈렸다면 피벗과 right가 가리키는 작은값을 바꾸고 while문 빠져나간다
            array[right], array[pivot] = array[pivot], array[right]
        else:
            array[left],array[right] = array[right],array[left]
    quick_sort(array,start,right-1) # 재귀적으로 계속 실행
    quick_sort(array,right+1,end)
    
quick_sort(array,0,len(array)-1)
print(array)
            
























    