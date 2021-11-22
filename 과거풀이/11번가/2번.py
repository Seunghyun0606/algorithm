# n*m 이 어차피 3만보다 작다.
# 리스트의 인덱스기준으로 리스트 문자열을 다 찾으면된다.

from collections import defaultdict

def solution(S):

    result = []

    list_length = len(S)
    word_length = len(S[0])

    for i in range(word_length):
        check_dict = defaultdict(list)
        for j in range(list_length):
            if check_dict[S[j][i]]:
                result += check_dict[S[j][i]]
                result.append(j)
                result.append(i)
                return result
            else:
                check_dict[S[j][i]] += [j]

    return result

