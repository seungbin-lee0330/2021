def solution(answers):
    
    answer = []
    one = [1,2,3,4,5] * 2000
    two = [2,1,2,3,2,4,2,5] * 1250
    three = [3,3,1,1,2,2,4,4,5,5] * 1000
    
    count_one = 0
    count_two = 0
    count_three = 0
    
    for i in range(len(answers)):
        
        if answers[i] == one[i]:
            count_one += 1
            
        if answers[i] == two[i]:
            count_two += 1
            
        if answers[i] == three[i]:
            count_three += 1
            
    count_set = [count_one,count_two,count_three]
    count_max = max(count_set)

    if count_one == count_max:

        answer.append(1)

    if count_two == count_max:

        answer.append(2)

    if count_three == count_max:

        answer.append(3)

    return answer