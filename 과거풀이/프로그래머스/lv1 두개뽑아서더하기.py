# 두개 뽑아서 더해서 나올 수 있는 모든 수 출력
# 조합으로 두개 뽑는다.

from collections import defaultdict

def solution(numbers):
    answer = []

    number_length = len(numbers)
    check_dict = defaultdict(int)

    for i in range(number_length-1):
        for j in range(i+1, number_length):
            if check_dict[numbers[i] + numbers[j]]:
                continue
            check_dict[numbers[i] + numbers[j]] = 1
    
    answer = sorted(list(check_dict.keys()))
    print(answer)

    return answer