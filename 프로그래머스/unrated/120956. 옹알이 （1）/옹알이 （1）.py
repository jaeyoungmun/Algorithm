def solution(babbling):
    answer = 0
    for i in range(len(babbling)):
        babbling[i] = babbling[i].replace("aya"," ") #공백문자 아니고 ""로 하면 wyeoo가 성립됨
        babbling[i] = babbling[i].replace("ye"," ")
        babbling[i] = babbling[i].replace("woo"," ")
        babbling[i] = babbling[i].replace("ma"," ")
        # print(babbling[i])
        babbling[i] = babbling[i].strip()
        if babbling[i] == "":
            # print("1")
            answer += 1
    return answer
