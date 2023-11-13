def solution(babbling):
    answer = 0
    for i in range(len(babbling)):
        babbling[i] = babbling[i].replace("aya"," ")
        babbling[i] = babbling[i].replace("ye"," ")
        babbling[i] = babbling[i].replace("woo"," ")
        babbling[i] = babbling[i].replace("ma"," ")
        # print(babbling[i])
        babbling[i] = babbling[i].strip()
        if babbling[i] == "":
            # print("1")
            answer += 1
    return answer