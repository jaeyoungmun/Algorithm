def solution(spell, dic):
    for i in dic:
        count = 0
        for j in range(len(spell)):
            if spell[j] in i:
                count += 1
            # print(count)
            if count == len(spell):
                return 1
    return 2