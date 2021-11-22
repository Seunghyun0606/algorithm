def solution(stones, k):
    answer = 0

    while True:
        i = 0
        while i < len(stones):
            if stones[i]:
                stones[i] -= 1
                i += 1
            else:
                for j in range(k):
                    if i + j <= len(stones) - 1:
                        if stones[i + j]:
                            i = i + j
                            break
                    else:
                        i = i + j
                        break
                else:

                    return answer
        answer += 1


solution( [2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3 )

