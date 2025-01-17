import sys
input = sys.stdin.readline
from itertools import combinations

n = int(input())
arr = []
nlist = []

for i in range(n):
    sub_arr = list(map(int, input().split()))
    arr.append(sub_arr)
    nlist.append(i)
    
mini_list = []

for i in combinations(nlist, n//2): #n개 중 n/2개 선택 (가능한 한 모든 조합이 완성될 때까지 반복문 진행)
    cnt = 0
    for j in combinations(i, 2): #선택된 n/2명 중 서로 서로의 시너지를 구하기 위해 또 조합 함수 사용
        cnt += arr[j[0]][j[1]] + arr[j[1]][j[0]]
        
    rest_list = list(set(nlist) - set(i))
    rest_cnt = 0
    for j in combinations(rest_list, 2): #조합에서 선택되지 않은 나머지 n/2개도 같은 방식으로 진행
        rest_cnt += arr[j[0]][j[1]] + arr[j[1]][j[0]]
    mini_list.append(abs(cnt-rest_cnt))
print(min(mini_list))