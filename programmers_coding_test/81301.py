def solution(s): # 문자열 그대로 다루고 바꿔버리는 replace 생각해내자...
    answer = 0
    english = ["zero","one","two","three","four","five","six","seven","eight","nine"]
    number = ["0","1","2","3","4","5","6","7","8","9"]
    for i in range(len(number)):   
        s = s.replace(english[i],number[i])
    answer = int(s)
    return answer