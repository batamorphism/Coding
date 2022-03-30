from collections import defaultdict


def main():
    n = int(input())
    A = list(map(int, input().split()))
    MOD = 998244353

    sum_a = 0
    bef_of = defaultdict(lambda: -1)
    DP = [0]*(n+1)
    DP[0] = 0
    bef = -1

    # 配るDP
    for i, a_i in enumerate(A, 1):
        # 次に足す要素がa_iで、
        # 次に参照する場所がDP[i]

        # i-1まで見たときの、区間和が0になる場所
        if i != 1:
            if bef == -1:
                # 0にならない
                DP[i] = DP[i-1]*2
            else:
                DP[i] = DP[i-1]*2
                # 重複分を除く
                # [bef+1, i-1]の和が0である
                DP[i] -= DP[bef]
            DP[i] %= MOD
        else:
            DP[i] = 1
        sum_a += a_i
        bef = bef_of[sum_a]
        bef_of[sum_a] = i

    ans = DP[n] % MOD
    print(ans)


main()
