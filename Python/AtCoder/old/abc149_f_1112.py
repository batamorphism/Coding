import sys
sys.setrecursionlimit(10**9)
mod = 10**9 + 7


def rev(num):
    # mod上でnum**-1を求める
    # a**(n-1) = 1 (mod n)
    return pow(num, mod-2, mod)


def main():
    n = int(input())
    nei_of = [[] for _ in range(n)]
    for i in range(n-1):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        nei_of[a].append((b, i))
        nei_of[b].append((a, i))

    # 各edgeに対しその左側と右側にあるnodeの数を求める
    cnt = [0]*(n-1)

    def dfs(cur, pre, cur_ind):
        ret = 1
        for nex, ind in nei_of[cur]:
            if nex != pre:
                ret += dfs(nex, cur, ind)
        if cur_ind >= 0:
            cnt[cur_ind] = ret
        return ret

    dfs(0, -1, -1)

    # Sのnodeの個数の平均値を求める
    # これは、各edgeについて、edgeの左右に黒が一つでもあれば+1される
    # ただし、初期値は1-2**(-n)  # 全て白の場合は除く

    # その後、Tに含まれる黒の個数はn/2となるので、
    # これを引けばよい
    # ans = 1 - 2**(-n)
    rev2 = rev(2)
    ans = 1 - pow(rev2, n, mod)
    for edge_cnt in cnt:
        le_cnt = edge_cnt
        ri_cnt = n - edge_cnt
        # ans += (1 - 2**(-le_cnt))*(1 - 2**(-ri_cnt))
        ans += (1 - pow(rev2, le_cnt, mod))*(1 - pow(rev2, ri_cnt, mod))
        ans %= mod
    ans -= n*rev2
    print(ans % mod)


main()
