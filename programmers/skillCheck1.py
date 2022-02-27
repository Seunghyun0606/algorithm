# 끝말 잇기

# n = 3
# words = ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]	

from collections import defaultdict

def solution(n, words):
    answer = [0, 0]
    word_dict = defaultdict(int)
    word_dict[words[0]] += 1
    # 2. 끝말 잇기 실패한 경우
    for i in range(1, len(words)):
        if words[i - 1][-1] != words[i][0]:
            return [ i % n + 1, i // n + 1 ]
            
    # 1. 이미 나온 단어 사용한 경우
        if word_dict[words[i]]:
            return [ i % n + 1, i // n + 1 ]
            
        word_dict[words[i]] += 1

    return answer

