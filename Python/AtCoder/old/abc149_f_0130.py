import sys
sys.setrecursionlimit(10**6)

# Sのサイズの平均値から、黒の数の平均値を引けばよい
MOD = 10**9+7
rev2 = (MOD+1)//2

def main():
    node_end = int(input())
    edge_end = node_end - 1
    nbd_of = [[] for _ in range(node_end)]
    for i in range(edge_end):
        fr, to = map(lambda x: int(x)-1, input().split())
        nbd_of[fr].append((to, i))
        nbd_of[to].append((fr, i))

    cnt_of = [0] * edge_end

    def dfs(cur, pre):
        ret = 1
        for nex, ind in nbd_of[cur]:
            if nex == pre:
                continue
            cnt = dfs(nex, cur)
            cnt_of[ind] = cnt
            ret += cnt
        return ret

    dfs(0, -1)

    ans = 1 - pow(rev2, node_end, MOD)
    for i in range(edge_end):
        head_side_node = node_end - cnt_of[i]
        leaf_side_node = cnt_of[i]
        prob = (1-pow(rev2, head_side_node, MOD)) * (1-pow(rev2, leaf_side_node, MOD))
        ans += prob
        ans %= MOD
    ans -= node_end * rev2
    ans %= MOD
    print(ans)


main()
