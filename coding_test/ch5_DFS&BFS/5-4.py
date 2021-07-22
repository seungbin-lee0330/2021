def recursive_function(i):
    
    if i == 100:
        return
    
    print(i, '번째 재귀 함수에서', i + 1 , '번째 재귀 함수를 호출합니다.')
    recursive_function(i+1)
    print(i, '번째 재귀 함수를 종료합니다')
    
recursive_function(1) # 재귀함수의 수행은 스택 자료구조를 이용한다. 따라서 100번째 재귀함수부터 차례대로 종료된다.