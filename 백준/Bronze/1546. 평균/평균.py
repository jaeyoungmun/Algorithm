n = int(input())
lst = list(map(int, input().split()))
best = lst[0]
sum =0
for i in range(1,n):
    if lst[i] > best:
        best = lst[i]

for i in range(n):
    sum += lst[i]

print((sum*100) / (best*n))