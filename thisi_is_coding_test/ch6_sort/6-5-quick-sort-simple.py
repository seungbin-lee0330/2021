array = [5,7,9,0,3,1,6,2,4,8]

def quick_sort(array): # 파이썬에 특화된 quick_sort 방식
    if len(array) <= 1:
        return
    pivot = array[0]
    tail = array[1:]
    left_side = [x for x in tail if x <= pivot]
    right_side = [x for x in tail if x > pivot]
    return quick_sort(left_side) + [pivot] + quick_sort(right_side)

print(quick_sort(array))










    