def solution(numbers, target):
    result = 0
    def dfs(num, level):
        nonlocal result

        if level == len(numbers):
            if num == target:
                result += 1
            return

        signs = [-num, num]
        if level == 1:
            for i in range(2):
                dfs(signs[i] + numbers[level], level + 1)
                dfs(signs[i] - numbers[level], level + 1)
        else:
            dfs(num + numbers[level], level + 1)
            dfs(num - numbers[level], level + 1)

    dfs(numbers[0], 1)
    return result



def solution(numbers, target):
    
    answer = 0
    
    def dfs(num,level):
        
        nonlocal answer
        
        if level == len(numbers):
            if num == target:
                answer += 1
            return
        
        first = [-num,num]
        if level == 1:
            for i in range(2):
                dfs(first[i] + numbers[level], level + 1)
                dfs(first[i] - numbers[level], level + 1)   

        else:
            dfs(num + numbers[level], level + 1)
            dfs(num - numbers[level], level + 1)

    dfs(numbers[0],1)

    return answer
