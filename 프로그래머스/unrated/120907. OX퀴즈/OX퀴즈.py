def solution(quiz):
    # print(quiz[0].replace("=","=="))
    answer = []
    for i in range(len(quiz)):
        quiz[i] = quiz[i].replace("=","==")
        if eval(quiz[i]) == True:
            answer.append("O")
        else:
            answer.append("X")
    return answer
#         space1 = tlr.find(" ")
#         equl = tlr.find("=")
#         op = tlr[space1+1:space1+2]
#         op_index = tlr.find(op) # 연산자의 인덱스
#         num1 = int(tlr[:space1])
#         num2 = int(tlr[op_index+1:equl-1])
#         result = int(tlr[equl+2:])
#         if op == "+":
#             if num1 + num2 == result:
#                 answer.append("O")
#             else:
#                 answer.append("X")
#         elif op == "-":
#             if num1 - num2 == result:
#                 answer.append("O")
#             else:
#                 answer.append("X")
            
#     return answer