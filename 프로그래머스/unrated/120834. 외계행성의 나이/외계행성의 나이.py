def solution(age):
    programmers_age = {'0': 'a', '1': 'b', '2': 'c','3':'d','4':'e','5':'f','6':'g','7':'h','8':'i','9':'j'}
    age = str(age)
    # print("사전value: ",programmers_age['2'])
    answer = ''
    for i in range(0,4):
        if age[i:i+1] == "":
            break
        new_age = age[i:i+1]
        # print(new_age)
        # print(programmers_age[new_age])
        answer += programmers_age[new_age]
    return answer