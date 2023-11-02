def solution(num_list):
    new_lst = []
    for i in range(1,len(num_list)+1):
        new_lst.append(num_list[-i])
    return new_lst