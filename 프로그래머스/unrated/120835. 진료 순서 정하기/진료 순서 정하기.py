def solution(emergency):
    new_list = []
    for i in range(len(emergency)):
        new_list.append(0)
    for new in range(1,len(emergency)+1):
        # print(new)
        for num in range(100,0,-1):
            if num in emergency:
                index = emergency.index(num)
                # print("new, num, index: ",new,num,index,"\n")
                emergency[index] = 0
                new_list[index] = new
                break
    
    return new_list