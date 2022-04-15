import sys, pypyjit
sys.setrecursionlimit
pypyjit.set_param('max_unroll_recursion=-1')


# 木DP
MOD = 10**9 + 7

def main():
    node_end = int(input())
    C = list(input().split())

    nei_of = [[] for _ in range(node_end)]
    for _ in range(node_end-1):
        fr, to = map(int, input().split())
        fr -= 1
        to -= 1
        nei_of[fr].append(to)
        nei_of[to].append(fr)

    # DP[node] = SubTree(node)における、辺の切り方のうち、
    #            全ての連結成分がa, b両方の文字を含む
    # DPA[node] = SubTree(node)における、辺の切り方のうち、
    #             nodeを含む連結成分がaのみを含む
    # DPB[node] = SubTree(node)における、辺の切り方のうち、
    #             nodeを含む連結成分がbのみを含む
    # DPC[node] = SubTree(node)における、辺の切り方のうち、
    #             nodeを含む連結成分がa, bのみを含むか、a, b両方とも含む
    DP = [0] * node_end
    DPA = [0] * node_end
    DPB = [0] * node_end

    def dfs(cur, pre):
        dpc = 1
        dpa = 1 if C[cur] == 'a' else 0
        dpb = 1 if C[cur] == 'b' else 0
        for nex in nei_of[cur]:
            if nex == pre:
                continue
            dfs(nex, cur)
            # 1. aについて
            # nexがaのみの場合は辺をつながねばならない
            # nexがa, b両方含む場合は、辺を切らなければならない
            dpa *= (DPA[nex]+DP[nex]) % MOD
            dpb *= (DPB[nex]+DP[nex]) % MOD
            # 2. cについて
            # C[cur] == 'a'のとき、
            # nexがaのみの場合は、辺をつながねばならない
            # nexがbのみの場合は、辺をつながねばならない
            # nexがa, b両方持つ場合は、辺をつないでもつながなくてもよい
            dpc *= (DPA[nex]+DPB[nex]+2*DP[nex]) % MOD
        DPA[cur] = dpa
        DPB[cur] = dpb
        DP[cur] = (dpc-dpa-dpb) % MOD

    dfs(0, -1)
    ans = DP[0]
    print(ans)


main()
