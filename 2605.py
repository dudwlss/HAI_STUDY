N = int(input())
lst = list(map(int, input().split()))
alst = [n for n in range(1, N+1)]

for i in range(N):
    n, t = lst[i], alst[i]
    for j in range(i, i-n, -1):  # 역순으로 접근
        alst[j] = alst[j-1]
    alst[i-n] = t  # 새로운 위치에 삽입
print(*alst)
