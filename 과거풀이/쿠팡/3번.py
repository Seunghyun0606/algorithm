from collections import defaultdict


def solution(k, score):
    answer = -1

    my_dict = defaultdict(list)
    check_dict = defaultdict(int)

    for i in range(len(score)-1):
        my_dict[score[i]-score[i+1]].append(i+1)
        if len(my_dict[score[i]-score[i+1]) >= k:
            check_dict[score[i]-score[i+1]] = 1
    result = 0
    for j in check_dict:
        k_list = my_dict[j]
        temp = 1
        for k in range(len(k_list)-1):
            if k_list[k+1] - k_list[k] == 1:
                temp += 1
            else:
                temp += 2
        result += temp

    return answer