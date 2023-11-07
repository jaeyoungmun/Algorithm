def solution(slice, n):
    # slice * pizza // n > 1이어야함
    for pizza in range(100):
        if pizza * slice / n >= 1:
            return pizza