from collections import defaultdict


def main():
    n = int(input())
    A = list(map(int, input().split()))
    bef_of = defaultdict(lambda: -1)
    MOD = 998244353

    # 貰うDP
    DP = [0]*n
    DP[0] = 1
    sum_a = A[0]
    for i, a_i in enumerate(A[1:], 1):
        # a_iを足す前の状態で
        # 足したら0になる区間を(le, ri]とする
        # (-INF, le]がダブルカウントになる
        le = bef_of[sum_a] - 1
        ri = i-1
        if le <= -1:
            DP[i] = 2*DP[i-1]
        else:
            DP[i] = 2*DP[i-1] - DP[le]
        bef_of[sum_a] = i
        sum_a += a_i
        DP[i] %= MOD
    ans = DP[n-1]
    print(ans)


main()
