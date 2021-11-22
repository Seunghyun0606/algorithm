def solution(d, budget):
    answer = 0
    d.sort()
    cnt = 0
    for m in d:
        if budget >= answer + m:
            answer += m
            cnt += 1
        else:
            return cnt
    else:
        return cnt