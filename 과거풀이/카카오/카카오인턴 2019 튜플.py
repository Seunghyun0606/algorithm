def solution(s):
    temp_list = []
    temp_str = ''
    temp = []
    for i in range(1, len(s) - 1):

        if 57 >= ord(s[i]) >= 48:
            temp_str += s[i]

        elif s[i] == '}':
            temp.append(temp_str)
            temp_str = ''
            temp_list.append(temp)
            temp = []

        elif s[i] == ',' and temp_str != '':
            temp.append(temp_str)
            temp_str = ''

    # 리스트 순서대로
    result_list = sorted(temp_list, key=lambda x: len(x))

    answer = []

    for result in result_list:
        for num in result:
            if int(num) in answer:
                continue
            answer.append(int(num))

    return answer