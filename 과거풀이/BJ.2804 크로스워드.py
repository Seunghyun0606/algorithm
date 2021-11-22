# Bj. 2804 크로스워드

word_a, word_b = input().split()

point_a = 0  # 가로 몇번째
point_b = 0  # 세로 에서 몇번째
flag = False
for a in range(len(word_a)):
    if flag:
        break
    for b in range(len(word_b)):
        if word_b[b] == word_a[a]:
            point_a = a
            point_b = b
            flag = True
            break

for b in range(len(word_b)):  #세로길이만큼 출력해야함
    my_print = ''
    for a in range(len(word_a)):  # 가로길이만큼 출력한다
        if a == point_a:
            my_print += word_b[b]
        else:
            my_print += '.'
    if b == point_b:
        print(word_a)
    else:
        print(my_print)
