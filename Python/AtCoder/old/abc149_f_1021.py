import sys
sys.setrecursionlimit(10**9)

mod = 10**9+7
rev2 = (mod+1)//2


def main():
    n = int(input())
    nei_of = [[] for _ in range(n)]
    for i in range(n-1):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        nei_of[a].append((b, i))
        nei_of[b].append((a, i))

    # 黒く塗られた頂点の組み合わせに対し、一つの部分木Sが定まる
    # したがって、各部分木Sの頂点数から、黒く塗られた頂点の個数を引けばよい
    # ある辺が部分木Sに含まれる確率は、
    # その辺より下にある頂点の数をx、上にある頂点の数をy(=n-x)とすれば、
    # 各xが全て白でなく、かつ各yが全て白でなければ良いので
    # (1-(1/2)**x)*(1-(1/2)**y)
    # これをすべての辺に対して合計すればよい
    color = ['w']*n
    # edge_cnt = 下にある頂点数
    edge_cnt = [0]*(n-1)

    def dfs(par):
        ret = 1
        for chi, ind in nei_of[par]:
            if color[chi] != 'w':
                continue
            color[chi] = 'g'
            cnt = dfs(chi)
            edge_cnt[ind] = cnt
            ret += cnt
        return ret

    color[0] = 'g'
    dfs(0)
    # print(edge_cnt)
    # 辺が存在すれば頂点数は辺の数+1
    # ただし、一切、頂点すら存在しない確率が(1/2)**2だけあるので除く
    ans = 1-pow(rev2, n, mod)
    ans %= mod
    for x in edge_cnt:
        y = n-x
        ans += (1-pow(rev2, x, mod))*(1-pow(rev2, y, mod))
        ans %= mod
    ans -= n*rev2
    print(ans % mod)


main()
