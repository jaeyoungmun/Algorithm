n = int(input())

lst = []
for _ in range(n):
    lst.append(int(input()))

for i in range(n):
    for j in range(i+1,n):
        if lst[i] > lst[j] :
            lst[i], lst[j] = lst[j], lst[i]

for i in range(n):
    print(lst[i])