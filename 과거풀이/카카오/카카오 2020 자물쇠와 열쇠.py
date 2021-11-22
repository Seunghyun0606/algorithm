# m x m 키를 전체 다돌린다. n >= m
# n x n 키 전체 다 확인한다음에, 회전시켜서 같은 작업 반복
# 0, 0, n-1 n-1까지 찾아야하니깐, n + m 패딩을 만들어야함.

def solution(key, lock):
    answer = True

    m = len(key)
    n = len(lock)

    for all_r in range(n):      # 키를 전체 돌리는 for 문
        for all_c in range(n):  # 키는 자물쇠를 벗어나도 된다. 단, 무조건 홈이 겹치면안됨
            for r in range(all_r, all_r + m):
                for c in range(all_c, all_c + m):
                    if n > r > -1 and n > c > -1:
                        



    return answer