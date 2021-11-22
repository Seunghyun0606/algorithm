def solution(arr, divisor):
    answer = []
    for num in arr:
        if not num % divisor:
            answer.append(num)
    else:
        if not answer:
            answer.append(-1)
    return sorted(answer
                  
# or 사용의 좋은 예제
# 앞이 참일 경우 앞이 되고, 빈 리스트면 뒤에꺼가 됨.
# def solution(arr, divisor): return sorted([n for n in arr if n%divisor == 0]) or [-1]