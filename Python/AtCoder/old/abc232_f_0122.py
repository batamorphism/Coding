# Aを、左から要素を確定させていく
# 既に確定させたAの要素からなる集合をSとする
# 配るDP
def main():
    n, x, y = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    ALL = 1 << n
    INF = float('inf')
    DP = [INF]*ALL
    DP[0] = 0

    for cur_S in range(ALL):
        # x not in S
        cur_n = popcount(cur_S)
        for i, a_i in enumerate(A):
            if cur_S >> i & 1:
                continue
            nex_S = cur_S | (1 << i)
            # i, a_iをn番目に持ってくる
            # [0, n-1]は既に埋まっている
            # したがって、i以下の、cur_Sに含まれない要素の数がswap回数
            lower_i_subset = ~cur_S & ((1 << i) - 1)
            swap_cnt = popcount(lower_i_subset)
            cost_y = swap_cnt * y
            cost_x = abs(B[cur_n] - a_i)*x
            DP[nex_S] = min(DP[nex_S], DP[cur_S] + cost_x + cost_y)

    print(DP[ALL - 1])


def popcount(S):
    return bin(S).count('1')


main()
