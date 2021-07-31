def solution(new_id): #문자열은 리스트 함수 사용한 수정이 안되고 슬라이싱으로 새롭게 정의해주는게 좋다
    answer = ''
    #1
    new_id = new_id.lower() # .lower()는 원본에 영향을 미치지 않는다
    #2
    for c in new_id:
        if c.isalpha() or c.isdigit() or c in ['-','_','.']:
            answer += c
    #3
    while '..' in answer: # 생각하기 어렵다 아니면 리스트로 바꿔서 적당히 손봐줘야 할듯
        answer = answer.replace('..', '.')
    #4
    if len(answer) > 1:
        if answer[0] == '.':
            answer = answer[1:]
        if answer[-1] == '.':
            answer = answer[:-1]
    else:
        if answer == '.':
            answer = ''
    #5
    if answer == '':
        answer = 'a'
    #6
    if len(answer) > 15:
        answer = answer[:15]
        if answer[-1] == '.':
            answer = answer[:-1]
    #7
    while len(answer) < 3:
        answer += answer[-1]
    return answer       
            