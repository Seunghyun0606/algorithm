from collections import defaultdict

def solution(participant, completion):

    check_dict = defaultdict(int)

    for man in completion:
        check_dict[man] += 1

    for man in participant:
        check_dict[man] -= 1

    for key, value in check_dict.items():
        if value == -1:
            return key