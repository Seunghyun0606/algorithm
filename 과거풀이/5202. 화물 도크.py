# 5202. 화물 도크

T = int(input())

for tc in range(T):
    n = int(input())
    time_table = []
    for _ in range(n): # 신청서 저장
        time_table.append(list(map(int, input().split())))
    time_table.sort(key=lambda e : e[1], reverse=True)# 빨리 끝나는 순으로 정렬
    result = 0
    work_done = 0 # 작업 끝난 시간
    while time_table:
        start_time, end_time = time_table.pop()
        if start_time >= work_done: # 작업 가능
            result += 1
            work_done = end_time # 작업 끝나는 시간 갱신
    print('#{}'.format(tc+1), result)