def solution(stones, k):
    left = 1
    right = 200000000
    while left <= right:
        mid = (left + right) // 2
        cnt = 0
        for i in range(len(stones)):
            if stones[i] <= mid:  # 여기서 stones[i] < mid이면 right값을 result로 내뿜어야한다.
                cnt += 1
                if cnt >= k:
                    right = mid - 1
                    break
            else:
                cnt = 0

        else:
            left = mid + 1
    return left

