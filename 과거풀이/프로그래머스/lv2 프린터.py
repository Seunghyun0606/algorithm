# 스택/큐

from collections import deque
def solution(priorities, location):
    answer = 0
    docs = deque(priorities)
    while docs:
        temp_doc = docs.popleft()
        location -= 1
        for doc in docs:
            if temp_doc < doc:
                docs.append(temp_doc)
                break
        else:
            answer += 1
            if location == -1:
                return answer
        if location == -1:
            location = len(docs) - 1
        
    return answer
solution([1, 1, 9, 1, 1, 1],	0)