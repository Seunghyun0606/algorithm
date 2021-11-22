# 문제 1 숫자이동


T = int(input())

for tc in range(T):
    time = int(input())

    line = list(map(int, input().split()))
    line2 = [0] * 10  # 라인이 for가 돌면서 겹칠수 있기 때문에 line2에 값을 더해줌, 이러면 겹치지 않음.
    for _ in range(time):
        for i in range(10):
            if abs(line[i]) >= 10:  # 규칙 3과 4를 함께고려
                if i == 9:
                    line2[i] += -(abs(line[i]) // 2)
                    line2[i-1] += -abs(line[i]) // 2
                elif i == 0:
                    line2[i] += (-abs(line[i]) // 2) * (-1)
                    line2[i-1] += abs(line[i]) // 2
                else:
                    line2[i+1] += abs(line[i]) // 2
                    line2[i-1] += -abs(line[i]) // 2
            else:                   # 규칙 3이 적용되지 않을 경우 규칙 1, 규칙2, 규칙 4 고려.
                if line[i] > 0:
                    if i == 9:
                        line2[i] += line[i]*(-1)
                    else:
                        line2[i+1] += line[i]
                    line[i] = 0
                elif line[i] < 0:
                    if i == 0:
                        line2[i] += line[i]*(-1)
                    else:
                        line2[i-1] += line[i]
            line[i] = 0         # line을 0으로만들어서 line2와 swap할때 초기화시키는 것.

        line, line2 = line2, line

    print('#{}'.format(tc+1), line)
