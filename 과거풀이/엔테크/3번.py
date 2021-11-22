# 단순하게 완전탐색하자
# 효율성에서 걸린다.


def solution(histogram):
    answer = 0

    length = len(histogram)
    for i in range(length-1):
        for j in range(i+1, length):
            h = min(histogram[i], histogram[j])
            w = j - i - 1
            answer = max(h*w, answer)


    return answer
