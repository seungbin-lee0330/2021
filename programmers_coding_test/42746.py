# 생각 못함
def solution(numbers):
    answer = ''
    numbers_str = [str(num) for num in numbers]
    numbers_str.sort(key=lambda num: num*3, reverse=True)       
    # num은 1000이하의 숫자이므로 x3(반복)한 값으로 비교
    # 자릿수가 다른 수들의 정렬을 생각하는 방법
    # 3 과 300 을 비교하면 3 이먼저 나와야 하는데 이는 333 과 300300300 을 비교한다
    if numbers_str[0] == '0': # 모두 0이라면 00000 이 아닌 0을 출력
        return '0'
    return ''.join(numbers_str)