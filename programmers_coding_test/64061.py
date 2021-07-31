def solution(board, moves):
    stacklist = []
    answer = 0

    for i in moves:
        for j in range(len(board)):
            if board[j][i-1] != 0: # 인형이 있는경우
                stacklist.append(board[j][i-1])
                board[j][i-1] = 0

                if len(stacklist) > 1: #인형이 2개이상 있는경우
                    if stacklist[-1] == stacklist[-2]:
                        stacklist.pop(-1)
                        stacklist.pop(-1)
                        answer += 2     
                break

    return answer
