# 하나씩 뽑고, a일때와 a가 아닐때로 구분, a가 아니면 +2 a면 이후 count검색

def solution(S):

    result = 0
    cnt = 0
    for s in S:
        if s == 'a':
            if cnt == 2:
                return -1
            cnt += 1

        else:
            if cnt == 1:
                result += 1
            elif cnt == 2:
                result += 0
            else:
                result += 2
            cnt = 0
    else:
        if cnt == 1:
            result += 1
        elif cnt == 0:
            result += 2

    return result