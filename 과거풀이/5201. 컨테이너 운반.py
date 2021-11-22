# 5201. 컨테이너 운반.

T = int(input())

for tc in range(T):
    n, m = map(int, input().split())
    # n, 컨테이너 갯수, m, 화물차 숫자

    loads = sorted(list(map(int, input().split())))
    trucks = sorted(list(map(int, input().split())))
    result = 0
    while trucks and loads:
        temp_t = trucks.pop()
        temp_loads = loads.pop()

        if temp_t >= temp_loads:
            result += temp_loads

        else:
            while loads:
                temp_loads = loads.pop()
                if temp_t >= temp_loads:
                    result += temp_loads

    print('#{}'.format(tc+1), result)




