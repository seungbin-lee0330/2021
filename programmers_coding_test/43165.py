answer = 0

def dfs(num,level,numbers,target):
        global answer
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
            
def solution(numbers, target):
    global answer
    dfs(numbers[0],1,numbers,target)
    return answer
