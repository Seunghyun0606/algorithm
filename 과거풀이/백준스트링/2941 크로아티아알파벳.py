alpha = [ 'c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

word = input()
cnt = len(word)
for alp in alpha:
    cnt -= word.count(alp)
    # if alp == 'dz=':
    #     cnt -= temp_cnt
    #     # cnt -= temp_cnt*2
    #     # cnt += temp_cnt
    # else:
    #     cnt -= temp_cnt
print(cnt)


# replace 사용법
# C=["c=","c-","dz=","d-","lj","nj","s=","z="]
# s=input()
# for i in C:s=s.replace(i,"!")
# print(len(s))