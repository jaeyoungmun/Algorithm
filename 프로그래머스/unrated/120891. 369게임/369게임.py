def solution(order):
    order = str(order)
    count = 0
    count += order.count('3')
    count += order.count('6')
    count += order.count('9')
    return count