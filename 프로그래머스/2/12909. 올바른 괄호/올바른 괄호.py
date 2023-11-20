def solution(s):
    stack = []
    # 팝 stack.pop()
    # 푸쉬 stack.append()
    # 엠티 len(stack) == 0
    # 탑 stack[-1]
    # print(s.pop())
    for i in s:
        if i == '(':
            stack.append(i)
        else:
            if len(stack) == 0:
                return False
            stack.pop()
    if len(stack) == 0:
        return True
    else:
        return False

