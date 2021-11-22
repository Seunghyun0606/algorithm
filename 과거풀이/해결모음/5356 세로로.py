# 5356. 의석이의 세로로 말해요


T = int(input())

for tc in range(T):

    words = [ list(map(str, input())) for _ in range(5) ]
    result_words = ''

    min_len = 0
    for word_len in words:  # max len 구해서 거기까지 반복하며 없애줄거야.
        temp_len = len(word_len)
        if min_len < temp_len:
            min_len = temp_len

    while min_len > 0:
        for i in range(len(words)-1, -1, -1):
            if len(words[i]) < 1:
                continue
            else:
                result_words = words[i].pop() + result_words
        min_len -= 1
    print('#{}'.format(tc+1), ''.join(result_words))