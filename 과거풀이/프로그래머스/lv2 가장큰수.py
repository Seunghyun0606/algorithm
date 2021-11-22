# numbers의 원소는 1000이하이고, string의 정렬을 위한 값 비교시,
# ascii로 변환해서 0번 인덱스부터 n-1번 까지 비교한다는점에 착안
# string을 int로 변환하고 다시 string으로 변환해서 리턴하는지 이해가 안됐는데
# 그렇게 join만 사용하면 0일 때가 문제다.
# [0,0,0,0] 을 input으로 넣는다면 '0000'이 리턴되므로 int로 변환해서 '0'으로 바꿔야 한다.
# 그리고 오버플로우 방지를 위해 다시 str으로 변환해야 하는 것!!!!

def solution(numbers):
    answer = ''
    num = list(map(str, numbers))

    num = sorted(num, key=lambda x : x*3, reverse=True)
    
    return str(int(''.join(num)))