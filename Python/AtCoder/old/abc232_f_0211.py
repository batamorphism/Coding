from functools import lru_cache


def main():
    n, x, y = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    ALL = 1 << n
    INF = float('inf')
    DP = [INF] * ALL
    DP[0] = 0

    # 配るDP
    for cur_S in range(ALL):
        for i, a_i in enumerate(A):
            if cur_S >> i & 1:
                continue
            nex_S = cur_S | 1 << i
            nex_pos = popcount(nex_S) - 1
            # cur_Sに含まれない要素のうち、i未満の者の数だけswapが必要
            cnt = popcount(~cur_S & (1 << i)-1)
            cost1 = y * cnt
            cost2 = x * abs(B[nex_pos] - a_i)
            DP[nex_S] = min(DP[nex_S], DP[cur_S] + cost1 + cost2)

    ans = DP[ALL-1]
    print(ans)


@lru_cache(maxsize=None)
def popcount(S):
    return bin(S).count('1')


main()
