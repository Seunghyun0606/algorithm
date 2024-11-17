
# 0 m 이상인 단어들만외운다
# 1 자주 나오는 단어일수록 앞에 배치한다.
# 2 해당 단어의 길이가 길수록 앞에 배치한다.
# 3 알파벳 사전 순으로 앞에 있는 단어일수록 앞에 배치한다

from collections import defaultdict
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

last_word_list = []

# 0. m 이상인 단어들만 뽑는다
word_list = [ val for _ in range(n) if len(val := input().rstrip()) >= m ]

my_dict = defaultdict(int)
for word in word_list:
    my_dict[word] += 1

# 1 자주 나오는 단어일수록 앞에 배치한다.
# 2 해당 단어의 길이가 길수록 앞에 배치한다.
# 3 알파벳 사전 순으로 앞에 있는 단어일수록 앞에 배치한다
sorted_word_list = sorted(my_dict.items(), key=lambda x : (-x[1], -len(x[0]), x[0]))

# print("====")
for word in sorted_word_list:
    print(word[0])




# Counter 써서 계산도가능
# from collections import Counter

# import sys
# input = sys.stdin.read
# data = input().splitlines()
# N, M = map(int, data[0].split())
# words = data[1:]

# # 단어의 길이가 M 이상인 단어만 고려
# filtered_words = [word for word in words if len(word) >= M]

# # 단어 빈도 계산
# word_count = Counter(filtered_words)

# # 정렬: -빈도, -길이, 사전순
# sorted_words = sorted(word_count.keys(), key=lambda x: (-word_count[x], -len(x), x))

# print('\n'.join(sorted_words))