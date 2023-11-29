def solution(numbers):
    # print(numbers.count())
    # -가 짝수개가 아닐때는 max찾아서 곱하기
    # -가 짝수개일때 브루트포스해버리기~!~!~!
    count = 0
    max_num = 0
    for i in range(len(numbers)):
        if numbers[i] < 0:
            count += 1
    if (count != 0) and (count % 2 == 0): #짝수개인 경우
        for i in range(len(numbers)-1):
            for j in range(1,len(numbers)):
                if i == j:
                    continue # 같은 원소끼리 곱하면 안됨
                if max_num < numbers[i] * numbers[j]:
                    max_num = numbers[i] * numbers[j]
        return max_num
    else:
        print("1")
        num1_idx = numbers.index(max(numbers))
        # print(num1_idx,num2_idx,"idx")
        num1 = numbers.pop(num1_idx)
        num2_idx = numbers.index(max(numbers))
        print("---",numbers)
        num2 = numbers.pop(num2_idx)
        return num1 * num2