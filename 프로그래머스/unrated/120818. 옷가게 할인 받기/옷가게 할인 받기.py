def solution(price):
    discount = 0
    if price >= 100000:
        discount = 0.05
    if price >= 300000:
        discount += 0.05
    if price >= 500000:
        discount += 0.1
    # print("discount: ",discount)
    return int(price * (1-discount))