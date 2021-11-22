# DP를 사용해서 리스트 슬라이싱으로 sum하는 시간을 줄인다.
# DP[k] = 해당 스테이지에 머무는 유저
# checck_state[k] = 해당 스테이지를 클리어한 유저.

def solution(N, stages):
    answer = []
    check_state = [0]*(N + 2)
    DP = [0]*(N + 2)
    for i in stages:
        check_state[i] += 1
    DP[N] = check_state[N+1]
    for j in range(N, 0, -1):
        DP[j] += DP[j+1] + check_state[j]
    
    for k in range(1, N+1):
        if DP[k]:
            answer.append((k, check_state[k]/DP[k] ))
        else:
            answer.append((k, 0))
    
    answer = sorted(answer, key=lambda x : -x[1])
    answer = [ i for i, k in answer ]

    return answer