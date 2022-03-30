import sys
import pypyjit
pypyjit.set_param('max_unroll_recursion=-1')
sys.setrecursionlimit(10**6)
cnt = 0


def main():
    node_end = int(input())
    nei_of = [[] for _ in range(node_end)]
    for _ in range(node_end - 1):
        a, b = map(lambda x: int(x) - 1, input().split())
        nei_of[a].append(b)
        nei_of[b].append(a)

    # leafに到達した順に、数値を打つ(hi = lo = cnt)
    # 戻り掛けに、hiとloを更新
    hi_of = [-1]*node_end
    lo_of = [-1]*node_end
    INF = float('inf')

    def dfs(cur, pre):
        global cnt
        hi = -INF
        lo = INF
        is_leaf = True
        for nex in nei_of[cur]:
            if nex == pre:
                continue
            is_leaf = False
            dfs(nex, cur)
            hi = max(hi, hi_of[nex])
            lo = min(lo, lo_of[nex])
        if is_leaf:
            hi = cnt
            lo = cnt
            cnt += 1
        hi_of[cur] = hi
        lo_of[cur] = lo

    dfs(0, -1)
    for hi, lo in zip(hi_of, lo_of):
        print(lo+1, hi+1)


main()
