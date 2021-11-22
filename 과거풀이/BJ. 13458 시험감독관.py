# BJ. 13458 시험감독관

n = int(input())  # 시험장갯수
people = list(map(int, input().split()))  # 각 시험장 사람 수
n_main, n_sub = map(int, input().split())  # 감독가능한 사람 수
result = 0
for person in people:
    if person - n_main < 0:
        result += 1
    else:
        if (person - n_main) % n_sub:
            result += 2 + (person - n_main) // n_sub
        else:
            result += 1 + (person - n_main) // n_sub
print(result)

