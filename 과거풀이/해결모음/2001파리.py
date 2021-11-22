# 2001. 파리 퇴치 D2

T = int(input())

for tc in range(T):

    n, m = map(int, input().split())
    array = [ list(map(int, input().split())) for _ in range(n) ]

    kill_count = 0
    for x in range(n-m+1):  # 최대거리까지 가서 거기서부터 m크기의 파리채에서의 킬량
        for y in range(n-m+1):
            new_count = 0
            for i in range(m):
                for j in range(m):
                    new_count += array[x+i][y+j]
            if new_count > kill_count:
                kill_count = new_count

    print('#{}'.format(tc+1), kill_count)



