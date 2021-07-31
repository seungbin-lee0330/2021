def solution(numbers, hand): # 쓰레기 코드...
    answer = ''
    left = [1,4,7,'*']
    mid = [2,5,8,0]
    right = [3,6,9,'#']
    left_idx = 3
    right_idx = 3
    for i in numbers:
        if i in [1,4,7]:
            answer += 'L'
            left_idx = left.index(i)
        if i in [3,6,9]:
            answer += 'R'
            right_idx = right.index(i)
        else:
            mid_idx = mid.index(i)
            if abs(left_idx - mid_idx) < abs(right_idx - mid_idx):
                answer += 'L'
            elif abs(left_idx - mid_idx) == abs(right_idx - mid_idx):
                answer += hand[0].upper()
            else:
                answer += 'R'
    return answer