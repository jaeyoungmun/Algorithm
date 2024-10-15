
import sys
input = sys.stdin.readline

lst = [int(input()) for _ in range(10)]
# print(lst)

for i in range(10):
    lst[i] = lst[i] % 42
# print("lst:",lst)
answer =[]

for i in lst:
    if i not in answer:
        answer.append(i)
print(len(answer))