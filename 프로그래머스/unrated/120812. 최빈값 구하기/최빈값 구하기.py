def solution(array):
    counter = {array[0] : 1}
    for i in range(1,len(array)):
        num = array[i]
        if num in counter:
            counter[num] += 1
        else:
            counter[num] = 1 
    max_value = max(counter.values())
    lst = [k for k, v in counter.items() if v == max_value]
    print("max_value: ",max_value)
    print("lst: ", lst)
    if len(lst) > 1:
        return -1
    elif len(lst) == 1:
        return lst[0]