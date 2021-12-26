# 木は辺で考える
# 答えの貢献度
# 各辺iに対し、その辺より後に出てくる頂点数をcnt_iとすると
# ans += cnt_i * (n - cnt_i)
import sys
sys.setrecursionlimit(10**6)


def main():
    n = int(input())
    nei_of = [[] for _ in range(n)]
    cnt_of = [0]*(n-1)

    for i in range(n-1):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        nei_of[a].append((b, i))
        nei_of[b].append((a, i))

    def dfs(cur, pre):
        ret = 1
        for nex, ind in nei_of[cur]:
            if nex == pre:
                continue
            cnt = dfs(nex, cur)
            # 戻り掛けに数える
            cnt_of[ind] = cnt
            ret += cnt
        return ret

    dfs(0, -1)

    ans = 0
    for cnt in cnt_of:
        ans += cnt*(n - cnt)
    print(ans)


main()
