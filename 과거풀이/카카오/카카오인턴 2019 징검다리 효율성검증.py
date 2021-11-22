# 사람이 지나갈때마다 stones의 숫자가 줄어든다
# 0이면 뛰어넘어가야한다
# 뛰어넘는 돌의 갯수가 k개 이면 종료한다

# 효율성을 증명하려면 모든 n과 k를 돌면안된다.
# 구간합이 제일 작은 구간에서의 최대값

# 한단계씩 올라가는 구간합은 맨 앞이랑 맨뒤값만 빼주면된다.

def solution(stones, k):
    init_sum = 0
    min_sum_index = -1
    min_sum = 10000000000
    for i in range(k):
        init_sum += stones[i]

    for i in range(len(stones) - k):
        temp = init_sum - stones[i] + stones[i + k]
        if temp < min_sum:
            min_sum = temp
            min_sum_index = i+1

        init_sum = temp

    # if min_sum_index == len(stones)-k:
    #     answer = max(stones[min_sum_index:])
    # else:
    answer = max(stones[min_sum_index:min_sum_index + k])
    print(min_sum_index)
    print(answer)


solution( [2, 4, 5, 3, 2, 4, 4, 2, 3, 1], 3 )

