# 맨처음 문자열의 length를 구하고, 1, 2, 4, 6, ... 나눌 수 있는 값을 구한다.
# "abcabcabcabcdededededede"
# "4abcdededededede" 3개씩 짜름

def solution(s):
    n = len(s)
    answer = n

    if n == 1:
        return 1

    count = 1
    num_slice = 1
    check_word = ''
    while num_slice <= n//2:
        temp = s[:num_slice]
        for i in range(num_slice, n, num_slice):

            word = s[i : i + num_slice]

            if word == temp:
                count += 1
            else:
                if count == 1:
                    check_word += temp
                    temp = word
                    continue
                check_word += str(count)
                check_word += temp

                count = 1
                temp = word
        if count != 1:
            check_word += str(count)
        check_word += temp

        count = 1

        num_slice += 1
        # print(check_word, answer)
        answer = min(answer, len(check_word))
        check_word = ''

    # print(answer)
    return answer
# a = "aabbaccc"
# solution(a)