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
        nei_of[a].append((i, b))
        nei_of[b].append((i, a))

    cnt_of = [0]*(n-1)
    # 各エッジに対して、それ以降の頂点がいくつあるか
    color = ['w']*n

    def dfs(pre_node):
        ret = 1
        for i, cur_node in nei_of[pre_node]:
            if color[cur_node] != 'w':
                continue
            color[cur_node] = 'g'
            tmp = dfs(cur_node)
            cnt_of[i] = tmp
            ret += tmp

        return ret

    color[0] = 'g'
    dfs(0)
    # 各辺に対し、その辺が木に含まれる確率は、
    ans = 0
    ans = 1-pow(rev2, n, mod)  # 1 - (1/2**(n))
    ans %= mod
    for edge in range(n-1):
        c = cnt_of[edge]
        edge_ans = (1-pow(rev2, c, mod))*(1-pow(rev2, n-c, mod)) % mod
        # (1-1/2**cnt_of[edge])*(1-1/2**(n-cnt_of[edge]))
        ans += edge_ans
        ans %= mod
    ans -= n*rev2
    ans %= mod
    print(ans)


main()
