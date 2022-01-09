# 小さい数から順番に位置を決めていく
# S=順番が決まった要素
# DP[null] = 1
# DP[S] = 0(条件を満たさないとき)
# DP[S] = sum_a in S (DP[S-a])
def main():
    n, m = map(int, input().split())
    A = [[] for _ in range(n+1)]
    for _ in range(m):
        x, y, z = map(int, input().split())
        A[y].append((x, z))

    ALL = 1 << n
    DP = [0] * ALL
    DP[0] = 1

    for s in range(1, ALL):
        ok = True
        cnt_s = popcount(s)
        for x, z in A[cnt_s]:
            # x以下の要素数がz以下か
            if popcount(((1 << x)-1) & s) > z:
                ok = False
                break
        if not ok:
            DP[s] = 0
            continue
        for i in range(n):
            if s & (1 << i):
                DP[s] += DP[s ^ (1 << i)]

    ans = DP[ALL-1]
    print(ans)


def popcount(x):
    return bin(x).count('1')


main()
