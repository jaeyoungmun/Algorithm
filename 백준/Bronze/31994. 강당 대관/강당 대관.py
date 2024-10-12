
import sys
input = sys.stdin.readline

dic = {}
for i in range(7):
    a, b = input().split()
    dic[a] = int(b)

# print(dic)
answer = max(dic, key=dic.get)
print(answer)