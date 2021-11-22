# 꽃
# 365개의 배열을 만들고, 거기서 해당하는 날짜에 값을 더해준다.
# 값이 있는 곳만 count


def solution(flowers):
    answer = 0
    
    flower_calender = [0]*366

    for flower in flowers:
        s, e = flower
        for i in range(s, e):
            if not flower_calender[i]:
                flower_calender[i] += 1
                answer += 1
    print(answer)

    return answer



