# 전체 시간을 1줄의 리스트로 만들어서 초당으로 계산한다. 60 -> 1분 3600 -> 1시간 360000 100시간
# 최대길이는 100시간이다 즉, 36만개 체크리스트 만들고, logs에 해당하는 위치에 있는 값이면 +1해준다.
# adv_time을 하나의 직선 (구간)으로 만들고, 가장 큰 구간을 찾는다.
# 시간초과;;;;;

def convert_time(time):
    h = int(time[:2])*3600
    m = int(time[3:5])*60
    s = int(time[6:])

    return h + m + s


def solution(play_time, adv_time, logs):
    answer = ''

    time = convert_time(play_time)

    play_check = [0] + [0]*time  # 1초부터 시작해서, 인덱스랑 초를 일치시킴

    for log in logs:
        start = log[:8]
        end = log[9:]
        start_time = convert_time(start)
        end_time = convert_time(end)
        for i in range(start_time, end_time):
            play_check[i] += 1
    
    ad_time = convert_time(adv_time)

    init_max_sum = sum(play_check[1 : ad_time+1])
    init_sum = init_max_sum
    index = 0
    for i in range(1, time - ad_time + 1):
        temp = init_sum - play_check[i] + play_check[i + ad_time]
        if temp > init_max_sum:
            init_max_sum = temp
            index = i+1
        init_sum = temp
    
    h = str(index // 3600)
    m = str(( index % 3600 ) // 60)
    s = str(( index % 3600 ) % 60)

    if len(h) < 2:
        h = '0' + h
    
    if len(m) < 2:
        m = '0' + m
    
    if len(s) < 2:
        s = '0' + s
    

    answer = h + ':' + m + ':' + s


    return answer

# a = "99:59:59"
# b = "25:00:00"
# c = ["69:59:59-89:59:59", "01:00:00-21:00:00", "79:59:59-99:59:59", "11:00:00-31:00:00"]
# solution(a, b, c)