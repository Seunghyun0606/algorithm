# 소문자, 대문자 구분안한다,
# 스펠링만 구별한다.

import math

def check(string):  # 소문자로만든다.
    temp = ''
    for s in string:
        if 65 <= ord(s) <= 90:     # 대문자를 소문자로 교체
            temp += chr(ord(s)+32)
        elif 97 <= ord(s) <= 122:  # 소문자
            temp += s
        else:
            temp += s
    return temp

def make_set(string):
    temp = []
    for i in range(len(string)-1):
        temp_str = ''
        if not ( 97 <= ord(string[i]) <= 122 ):
            continue
        if not ( 97 <= ord(string[i+1]) <= 122 ):
            continue

        temp_str += string[i]
        temp_str += string[i+1]
        temp.append(temp_str)
    return temp

def many(bigger, smaller):
    check = [0]*len(bigger)
    inter_count = 0
    for i in range(len(smaller)):
        for j in range(len(bigger)):
            if check[j]:
                continue
            if smaller[i] == bigger[j]:
                check[j] = 1
                inter_count += 1
                break
    return len(bigger) + len(smaller) - inter_count, inter_count  # 합집합, 교집합 갯수.

def solution(str1, str2):
    answer = 65536

    my_str1 = check(str1)
    my_str2 = check(str2)

    my_list1 = make_set(my_str1)
    my_list2 = make_set(my_str2)

    if my_list1 == my_list2:
        return answer
    else:
        a = len(my_list1)
        b = len(my_list2)
        
        if a >= b:
            union, inter = many(my_list1, my_list2)
        else:
            union, inter = many(my_list2, my_list1)
    

    answer = math.trunc((inter/union)*65536)  # 소수점 버림

    # print(answer)
    # print(inter/union)
    # print(union)
    # print(inter)
    # print(my_str1)
    # print(my_str2)
    # print(my_list1)
    # print(my_list2)
    return answer

# a, b = 'aa1+aa2', 'AAAA12'

# solution(a, b)
