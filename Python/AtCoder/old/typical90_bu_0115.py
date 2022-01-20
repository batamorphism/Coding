# rootを0とする
# 末尾からDPをする
# DP[node] = そのnode以下のsubtreeにおける、切り方の組み合わせ数
# DP[node][0] = nodeを含む連結成分がaのみ
# DP[node][1] = nodeを含む連結成分がbのみ
# DP[node][2] = nodeを含む連結成分がaとbの両方を含む
# DP[node][3] = 全ての切り方の和
# sum(DP[node]) は
# nodeがaの場合、DP[node][1] = 0、DP[node][0] = 全てのpreがDP[pre][0]、
def main():
    MOD = 10**9+7
    node_end = int(input())
    C = list(input().split())
    nei_of = [[] for _ in range(node_end)]

    for _ in range(node_end-1):
        fr, to = map(lambda x: int(x)-1, input().split())
        nei_of[fr].append(to)
        nei_of[to].append(fr)
    DP = [[0]*3 for _ in range(node_end)]

    def dfs(cur, pre):
        if C[cur] == 'a':
            dpa = 1
            dpb = 0
        else:
            dpa = 0
            dpb = 1
        dpall = 1  # aとbが完全に独立してしまわない
        for nex in nei_of[cur]:
            if nex == pre:
                continue
            dfs(nex, cur)
            if C[cur] == 'a':
                # a->aを切らないパターンと、
                # a->abを切るパターン
                dpa *= (DP[nex][0] + DP[nex][2])
            elif C[cur] == 'b':
                dpb *= (DP[nex][1] + DP[nex][2])
            dpall *= (DP[nex][0] + DP[nex][1] + DP[nex][2]*2)
            dpa %= MOD
            dpb %= MOD
            dpall %= MOD
        DP[cur][0] = dpa
        DP[cur][1] = dpb
        DP[cur][2] = dpall-dpa-dpb
        DP[cur][2] %= MOD

    dfs(0, -1)
    print(DP[0][2])


main()
