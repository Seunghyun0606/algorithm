# 초당 최대 처리량 계산하기
# lines 배열, N개 로그 문자열
# 응답완료시간 S와 처리시간 T가 공백으로 구분
# 응답완료시간은 고정길이 2016-09-15 hh:mm:ss.sss 형식
# 처리시간 T는 최대소수점 셋째 짜리까지 기록. 뒤에는 초 단위 s를 붙인다. 0.312s
# 타임아웃은 3초, 처리시간은 0.001 <= T <= 3.000
# lines배열은 응답완료시간 S를 기준으로 오름차순 정렬
# 초당 최대 처리량 Return

lines = [

"2016-09-15 01:00:04.001 2.0s",
"2016-09-15 01:00:07.000 2s"

]

# 1시간 = 60*60*1000
# 1분 = 60 * 1000 * 1mm초
# 1초 = 1000 * 1mm초

logs = []

for line in lines:
    date, S, T = line.split()
    hours, minutes, seconds = S.split(':')
    seconds, miliseconds = map(int, seconds.split('.'))

    mHours = int(hours) * 60 * 60 * 1000
    mMinutes = int(minutes) * 60 * 1000
    mSeconds = seconds * 1000

    end_time = mHours + mMinutes + mSeconds + miliseconds

    T = int(float(T.rstrip('s')) * 1000 )

    # start, end time
    logs.append([end_time - T + 1, end_time])

answer = 0

for i in range(len(logs)):
    cnt = 0
    cur_end_time = logs[i][1]

    for j in range(i, len(logs)):
        if cur_end_time > logs[j][0] - 1000:
            cnt += 1
    
    answer = max(answer, cnt)

return answer







