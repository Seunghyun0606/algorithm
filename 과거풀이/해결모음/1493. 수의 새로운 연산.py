# 1493. 수의 새로운 연산 D3


def my_cordi(result, x=-1, y=-1):

    if x == -1 and y == -1:  # 값을 넣엇을때의 좌표값 구하기
        n = 0
        my_number = 0
        flag = True
        while flag:  # (x, 1) 일때의 값을 만들었다. 이걸바탕으로 좌표값을 구할 거다.
            n += 1   # 여기서 n 값이 x일때의 위치.
            my_number += n

            if my_number == result:
                return n, 1
            if my_number > result:
                y = 1  # n이 x값과 같으니깐 y 값만 구해내면된다
                while flag:
                    my_number -= 1
                    n -= 1
                    y += 1
                    if my_number == result:
                        return n, y
    else:
        n = 0
        my_number = 0
        while n < x:  # (x, 1) 일때의 값을 만들었다. (2, 1) 일 때 3이된다.
            n += 1
            my_number += n

        n = 1  # 이미 (x, 1) 위치에서의 값이 있기 때문이다.
        while n < y:  # (x, y)에서의 값, (x, 1) 일때의 값에서 y일때 더해올라간다.
            n += 1
            my_number += x
            x += 1
        # 좌표값을 넣었을때 결과값
        return my_number

T = int(input())

for tc in range(T):
    p, q = map(int, input().split())

    a, b = my_cordi(p)
    c, d = my_cordi(q)

    final_result = my_cordi(0, x=a+c, y=b+d)

    print('#{}'.format(tc+1), final_result)