# 많이 어려운 문제 나중에 다시풀기

class Node:
    def __init__(self):
        self.alpha = {}
        self.count = 0

class Trie:
    def __init__(self):
        self.root = Node()
        
        
    def insert(self, word):
        temp = self.root
        
        for w in word:
            if temp.alpha.get(w):
                temp = temp.alpha[w]
            else:
                temp.alpha[w] = Node()
                temp = temp.alpha[w]
            temp.count += 1
    
    def search(self, que):
        cnt = 0
        if que == '':
            for val in self.root.alpha.values():
                cnt += val.count
            return cnt
        temp = self.root
        for w in que:
            if temp.alpha.get(w):
                temp = temp.alpha[w]
                cnt = temp.count
            else:
                return 0
        return cnt
    
    
def solution(words, queries):
    t_a = [Trie() for i in range(10001)]
    r_a = [Trie() for i in range(10001)]
    
    # words => Tries
    for word in words:
        t_a[len(word)].insert(word)
        r_a[len(word)].insert(word[::-1])
        
    # Search => queries
    answer = [0 for _ in range(len(queries))]
    for idx, que in enumerate(queries):
        if que[0] != '?': # queries => t_a
            s_que = que.split('?')[0]
            answer[idx] = t_a[len(que)].search(s_que)
        else: # queries => r_a
            s_que = que.split('?')[-1]
            answer[idx] = r_a[len(que)].search(s_que[::-1])
    
    return answer