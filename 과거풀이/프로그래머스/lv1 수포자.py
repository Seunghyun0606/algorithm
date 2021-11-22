def solution(answers):
    answer = [0]*3

    person1 = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
    person2 = [2, 1, 2, 3, 2, 4, 2, 5]  # 2
    person3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]  # 2개 반복
    
    n = 0
    k = 0
    for i in range(len(answers)):
        ans = answers[i]
        if i // 10:
            n = i // 10
        if i // 8:
            k = i // 8
        if ans == person1[i-10*n]:
            answer[0] += 1
        if ans == person2[i-8*k]:
            answer[1] += 1
        if ans == person3[i-10*n]:
            answer[2] += 1

    ans_max = max(answer)
    result = []
    for j in range(3):
        if answer[j] == ans_max:
            result.append(j+1)
    return result




# 패턴을 generator로써 처리하여 공간복잡도까지 고려가 된 코드네요. 잘봤습니다.
# from itertools import cycle

# def solution(answers):
#     giveups = [
#         cycle([1,2,3,4,5]),
#         cycle([2,1,2,3,2,4,2,5]),
#         cycle([3,3,1,1,2,2,4,4,5,5]),
#     ]
#     scores = [0, 0, 0]
#     for num in answers:
#         for i in range(3):
#             if next(giveups[i]) == num:
#                 scores[i] += 1
#     highest = max(scores)

#     return [i + 1 for i, v in enumerate(scores) if v == highest]

# 깔끔하게 작성한 코드
# 각 패턴마다 주기가 다르기때문에, 주기계산을 위해서 나머지를 사용함.
# def solution(answers):
#     pattern1 = [1,2,3,4,5]
#     pattern2 = [2,1,2,3,2,4,2,5]
#     pattern3 = [3,3,1,1,2,2,4,4,5,5]
#     score = [0, 0, 0]
#     result = []

#     for idx, answer in enumerate(answers):
#         if answer == pattern1[idx%len(pattern1)]:
#             score[0] += 1
#         if answer == pattern2[idx%len(pattern2)]:
#             score[1] += 1
#         if answer == pattern3[idx%len(pattern3)]:
#             score[2] += 1

#     for idx, s in enumerate(score):
#         if s == max(score):
#             result.append(idx+1)

#     return result