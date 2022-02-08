import sys
sys.setrecursionlimit(10**6)


# 木DP
def main():
    node_end = int(input())
    col = list(input().split())
    nei_of = [[] for _ in range(node_end)]
    for _ in range(node_end-1):
        a, b = map(lambda x: int(x)-1, input().split())
        nei_of[a].append(b)
        nei_of[b].append(a)
    MOD = 10**9 + 7

    # 木DP
    def dfs(cur, pre):
        if col[cur] == 'a':
            dp_a = 1
            dp_b = 0
            dp_s = 1
        else:
            dp_a = 0
            dp_b = 1
            dp_s = 1

        for nex in nei_of[cur]:
            if nex == pre:
                continue
            nex_dp_a, nex_dp_b, nex_dp_ab = dfs(nex, cur)
            dp_a *= (nex_dp_a + nex_dp_ab)
            dp_b *= (nex_dp_b + nex_dp_ab)
            dp_s *= (nex_dp_a + nex_dp_b + nex_dp_ab * 2)
            dp_a %= MOD
            dp_b %= MOD
            dp_s %= MOD
        dp_ab = dp_s - dp_a - dp_b
        dp_ab %= MOD
        return dp_a, dp_b, dp_ab

    a, b, ab = dfs(0, -1)
    print(ab)


main()
