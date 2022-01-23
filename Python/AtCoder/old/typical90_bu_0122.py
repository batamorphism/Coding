import sys
sys.setrecursionlimit(10**6)


# 木DP
# 貰うDP
def main():
    MOD = 10**9 + 7
    n = int(input())
    C = list(input().split())
    nei_of = [[] for _ in range(n)]
    for _ in range(n-1):
        fr, to = map(lambda x: int(x)-1, input().split())
        nei_of[fr].append(to)
        nei_of[to].append(fr)

    DPA = [0]*n
    DPB = [0]*n
    DPAB = [0]*n

    def dfs(cur, pre):
        dpall = 1
        if C[cur] == 'a':
            dpa = 1
            dpb = 0
        else:
            dpa = 0
            dpb = 1
        for nex in nei_of[cur]:
            if nex == pre:
                continue
            dfs(nex, cur)
            # sub_treeから貰うDP
            dp_child_a = DPA[nex]
            dp_child_b = DPB[nex]
            dp_child_ab = DPAB[nex]
            dpa *= (dp_child_a + dp_child_ab)
            dpb *= (dp_child_b + dp_child_ab)
            dpall *= (dp_child_a + dp_child_b + dp_child_ab*2)
            dpa %= MOD
            dpb %= MOD
            dpall %= MOD
        dpab = dpall - dpa - dpb
        dpab %= MOD
        # print(cur+1, dpa, dpb, dpall, dpab)
        DPA[cur] = dpa
        DPB[cur] = dpb
        DPAB[cur] = dpab

    dfs(0, -1)

    ans = DPAB[0]
    print(ans)


main()
