# 2016년, 윤년, 366일
# 1 3 5 7 8 10 12 31일
# 2 29일 4 6 9 11 30일

def solution(a, b):
    answer = ''

    days = [0]*13  # 1월부터시작하기 위함, 누적 days를 저장할거임
    for i in range(1, 13):
        if i in (4, 6, 9, 11):
            days[i] = days[i-1] + 30
        elif i == 2:
            days[i] = days[i-1] + 29
        else:
            days[i] = days[i-1] + 31
    
    weeks = ['THU', 'FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED']
    answer = weeks[( days[a-1] + b ) % 7]
    return answer