import sys
sys.setrecursionlimit(10**6)

# (u, v): u < vの組に対して、距離の総和を求めよ
# u->vが最短距離に何回含まれるか

def main():
    n = int(input())
    nei_of = [[] for _ in range(n)]
    for i in range(n-1):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        nei_of[u].append((v, i))
        nei_of[v].append((u, i))

    # 各edgeについて、そのedge以下の部分木のサイズを求める
    cnt = [0] * (n-1)

    def dfs(cur, pre):
        ret = 1
        for nex, ind in nei_of[cur]:
            if nex != pre:
                tmp = dfs(nex, cur)
                cnt[ind] = tmp
                ret += tmp
        return ret

    dfs(0, -1)

    # 各edgeは、cnt*(n-cnt)回含まれるのでこれが貢献度
    ans = 0
    for edge in range(n-1):
        ans += cnt[edge] * (n-cnt[edge])

    print(ans)


main()
