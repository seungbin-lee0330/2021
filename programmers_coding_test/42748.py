def solution(array, commands):
    answer = []
    
    for i in range(len(commands)):
        start = commands[i][0]
        end = commands[i][1]
        index = commands[i][2]
        
        new_array = array[start-1:end]
        new_array.sort()
        number = new_array[index - 1]
        answer.append(number)
    
    return answer