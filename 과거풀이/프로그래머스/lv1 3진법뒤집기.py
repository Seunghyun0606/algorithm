# n을 3진법으로 만들고, 뒤집고, 10진법으로 만들기
# 45 -> 1200(3) 27 18 15 5 1 2
# 애초에 3진법을 처음부터 만들면, 뒤집을 필요가없는데?
def solution(n):
    answer = 0

    my_num = ''

    while n:
        my_num += str(n % 3)
        n = n // 3
    
    ans_num = str(int(my_num))
    cnt = 0
    for i in range(len(ans_num)-1, -1, -1):
        answer += int(ans_num[i])*3**cnt
        cnt += 1
    return answer