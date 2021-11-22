# 1단계 new_id의 모든 대문자를 대응되는 소문자로 치환합니다.
# 2단계 new_id에서 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자를 제거합니다.
# 3단계 new_id에서 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환합니다.
# 4단계 new_id에서 마침표(.)가 처음이나 끝에 위치한다면 제거합니다.
# 5단계 new_id가 빈 문자열이라면, new_id에 "a"를 대입합니다.
# 6단계 new_id의 길이가 16자 이상이면, new_id의 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거합니다.
#      만약 제거 후 마침표(.)가 new_id의 끝에 위치한다면 끝에 위치한 마침표(.) 문자를 제거합니다.
# 7단계 new_id의 길이가 2자 이하라면, new_id의 마지막 문자를 new_id의 길이가 3이 될 때까지 반복해서 끝에 붙입니다.

# 48 57 0 ~ 9
# a 97 122 (25) (32)
# A 65 90
def step2(word):

    # 쓸모없는 문자제거
    sign = { '-': True, '_': True, '.': True }

    new_word = ''

    for w in word:
        if w in sign or 48 <= ord(w) <= 57 or 97 <= ord(w) <= 122:
            new_word += w

    return new_word

def step3(word):

    i = 0
    new_word = ''
    while i < len(word):
        flag = True
        if word[i] == '.':
            i += 1
            while i < len(word):
                if word[i] != '.':
                    flag = False
                    break
                i += 1
            new_word += '.'
        else:
            new_word += word[i]

        if flag:
            i += 1
    return new_word



def solution(new_id):
    answer = ''

    # step1 소문자변환
    new_id = new_id.lower()

    # step2
    new_id = step2(new_id)

    # step3 . 중복제거
    new_id = step3(new_id)

    # step4 . 양끝제거
    if new_id[0] == '.' and new_id[-1] == '.':
        new_id = new_id[1:-1]
    elif new_id[0] == '.':
        new_id = new_id[1:]
    elif new_id[-1] == '.':
        new_id = new_id[:-1]

    # step5 빈문자열이면 'a'
    if not new_id:
        new_id += 'a'
    
    # step6 길이 16이상이면 나머지제거
    if len(new_id) > 15:
        new_id = new_id[:15]

        if new_id[-1] == '.':
            new_id = new_id[:-1]
    # step7 길이가 2이하이면 마지막문자를 new_id 3이 될때까지 반복하여 끝에 붙임

    if len(new_id) <= 2:
        last_word = new_id[-1]
        while len(new_id) < 3:
            new_id += last_word

    answer = new_id
    

    return answer
