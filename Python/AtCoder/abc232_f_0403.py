def main():
    n, x, y = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    # 左からいくつかだけ合わせるのにかかるコストを考える
    # Aのうち、既に採用した要素をSとする
    S_end = 1 << n
    INF = float('inf')
    DP = [INF] * (S_end + 1)
    DP[0] = 0

    for pre_S in range(S_end):
        pre_n = popcount(pre_S)
        # A[:pre_n-1]が既に確定している
        pre_cost = DP[pre_S]
        # 配るDP
        for cur_node in range(n):
            if pre_S & (1 << cur_node):
                continue
            cur_S = pre_S | (1 << cur_node)
            cur_b = B[pre_n]
            cur_a = A[cur_node]
            cost1 = abs(cur_a-cur_b)*x
            # cur_nodeを何回スワップさせる必要があるか
            # pre_Sのうち、cur_node未満の要素が0となっている個数を数えればよい
            # つまり、~pre_Sのうち、cur_node未満の要素で1となっている者を数えればいい
            counter = ~pre_S & ((1 << cur_node) - 1)
            swap_cnt = popcount(counter)
            cost2 = swap_cnt * y
            DP[cur_S] = min(DP[cur_S], pre_cost + cost1 + cost2)

    ans = DP[S_end-1]
    print(ans)


def popcount(S):
    return bin(S).count('1')


main()
