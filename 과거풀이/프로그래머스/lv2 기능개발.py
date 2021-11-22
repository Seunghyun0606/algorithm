# 스택/큐 활용이긴한데, 그냥 k로도 가능할거같아서 그냥함

# from collections import deque

def solution(progresses, speeds):
    answer = []
    n = len(speeds)
    # prog = deque(progresses)
    # spee = deque(speeds)
    k = 0
    for _ in range(100):
        cnt = 0
        for i in range(k, n):
            progresses[i] += speeds[i]
        while k < n and progresses[k] > 99:
            cnt += 1
            k += 1
            # prog.leftpop()
            # spee.leftpop()
        if cnt:
            answer.append(cnt)
        if k == n:
            return answer        
    return answer