# 全部nになったら操作打ち切り
# 実直なシミュレーションを行う
def main():
    n, k = map(int, input().split())
    A = list(map(int, input().split()))
    for _ in range(k):
        imos = [0]*(n+1)
        for i, a in enumerate(A):
            le = max(i-a, 0)
            ri = min(i+a, n-1)
            imos[le] += 1
            imos[ri+1] -= 1
        for i in range(1, n+1):
            imos[i] += imos[i-1]
        A = imos[:n]
        if sum(A) == n**2:
            # 終局状態
            break
    print(*A)


main()
