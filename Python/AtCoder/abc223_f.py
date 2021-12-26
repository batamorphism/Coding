from functools import lru_cache
import sys
sys.setrecursionlimit(10**6)


# 1+...+1000=(1+1000)*1000/2
# 並び替え可能であれば、合計5*10**5回以下にできる
def main():
    n = int(input())
    P = list(map(int, input().split()))
    P = [p-1 for p in P]

    P_rev = [0]*n
    for i, p_i in enumerate(P):
        P_rev[p_i] = i

    # setup union find
    par = [i for i in range(n)]

    def find(x):
        if x == par[x]:
            return x
        par[x] = find(par[x])
        return par[x]

    def union(x, y):
        x = find(x)
        y = find(y)
        if x == y:
            return
        par[x] = y

    def same(x, y):
        return find(x) == find(y)

    m = int(input())
    swap_list = []
    nei_of = [[] for _ in range(n)]
    for i in range(m):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        if a > b:
            a, b = b, a
        swap_list.append((a, b, i))
        union(a, b)
        nei_of[a].append((b, i))

    # check
    for i, p in enumerate(P):
        if not same(i, p):
            print(-1)
            return

    @lru_cache(maxsize=None)
    def dfs(pre, target):
        # pre -> targetに行くまでに通るedgeのindex
        ret1 = []
        ret2 = False
        if pre == target:
            return tuple(ret1), True
        for cur, ind in nei_of[pre]:
            tmp1, tmp2 = dfs(cur, target)
            if tmp2:
                for t in tmp1:
                    ret1.append(t)
                ret1.append(ind)
                ret2 = True
                break
        return tuple(ret1), ret2

    # make_ans
    ans_list = []
    for i in range(n):
        edge_list, _ = dfs(i, P_rev[i])
        # print(edge_list)
        for edge in edge_list:
            a, b, i = swap_list[edge]
            P_rev[P[a]], P_rev[P[b]] = P_rev[P[b]], P_rev[P[a]]
            P[a], P[b] = P[b], P[a]
            ans_list.append(i+1)
        # iとp_iと結ぶedgeを探す

    # print(P)
    print(len(ans_list))
    print(*ans_list)


main()
