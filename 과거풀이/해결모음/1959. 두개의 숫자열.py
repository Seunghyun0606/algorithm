# 1959. 두개의 숫자열 D2

T = int(input())

for tc in range(T):
    n, m = map(int, input().split())  # A와 B의 숫자 갯수

    a_list = list(map(int, input().split()))
    b_list = list(map(int, input().split()))

    # abs(len(long) - len(short)) +1 -> 움직일수 있는거리 (작은쪽이 움직이면서 곱해나가야함)

    if len(a_list) > len(b_list):
        short = b_list
        longer = a_list
    else:
        short = a_list
        longer = b_list

    max_result = 0
    for i in range(len(longer)-len(short)+1):  # 짧은 배열을 오른쪽으로 움직일것
        result = 0
        for x in range(len(short)):  # short 길이만큼 그때의 좌표값을 곱해준다.
            result += (short[x] * longer[x+i])
        if result > max_result:
            max_result = result

    print('#{}'.format(tc+1), max_result)