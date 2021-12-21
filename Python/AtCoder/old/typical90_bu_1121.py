# DPA[node] nodeを含む部分木がaしか含んでおらず、それ以外の切断された部分木がa, b両方含むときの切断方法
# DPB[node] nodeを含む部分木がbしか含んでおらず、それ以外の切断された部分木がa, b両方含むときの切断方法
# DPC[node] nodeを含む部分木がa, b両方含むときの切断方法
# DPA+BPB+DPC = 全ての切断方法
# nodeがaの時
# DPA[node] = PRODUCT(DPA[child]  # node->childを切断しない
#             + DPC[child])  # node->childを切断
# DPB[node] = 0
# DPC[node] = ALL - DPA[node]
# ALL = PRODUCT(DPA[child]  # node->childを切断しない
#               DPB[child])  # node->childを切断しない
#               2*DPC[child])  # node->childを切断してもしなくてもよい
mod = 10**9 + 7


def main():
    n = int(input())
    tree = list(input().split())
    nei_of = [[] for _ in range(n)]
    for _ in range(n-1):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        nei_of[a].append(b)
        nei_of[b].append(a)

    # tree DP
    DPA = [-1]*n
    DPB = [-1]*n
    DPC = [-1]*n

    def dfs(cur, pre):
        dpa = 0
        dpb = 0
        all = 1
        if tree[cur] == 'a':
            dpa = 1
        else:
            dpb = 1
        for nex in nei_of[cur]:
            if nex == pre:
                continue
            dfs(nex, cur)
            dpa *= (DPA[nex] + DPC[nex]) % mod
            dpb *= (DPB[nex] + DPC[nex]) % mod
            all *= (DPA[nex] + DPB[nex] + DPC[nex]*2) % mod
        DPA[cur] = dpa
        DPB[cur] = dpb
        DPC[cur] = (all - dpa - dpb) % mod
        return

    dfs(0, -1)

    print(DPC[0])


main()
