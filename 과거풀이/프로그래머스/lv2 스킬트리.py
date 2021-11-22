from collections import defaultdict
def solution(skill, skill_trees):
    answer = 0
    check_dict = defaultdict(int, zip(skill, [1]*len(skill)))
    for skill_tree in skill_trees:
        k = 0
        for i in range(len(skill_tree)):
            if check_dict[skill_tree[i]]:
                if skill_tree[i] == skill[k]:
                    k += 1
                    if k == len(skill):
                        answer += 1
                        break
                else:
                    break
        else:
            answer += 1
    return answer