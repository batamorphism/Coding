import sys
sys.setrecursionlimit(10**9)


def main():
    n = int(input())
    nei_of = [[] for _ in range(n)]
    for i in range(n-1):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        nei_of[a].append(b)
        nei_of[b].append(a)
    q = int(input())
    query = []
    for _ in range(q):
        k, *v = list(map(int, input().split()))
        v = [vv-1 for vv in v]
        v = set(v)
        query.append((k, v))

    for k, v in query:
        print(solver(k, v, n, nei_of))


def solver(k, v: set, n, nei_of):
    # 木DP
    DP = [-1]*n

    def dfs(pre_node):
        DP[pre_node] = 0
        if pre_node in v:
            cnt = 1
        else:
            cnt = 0
        for cur_node in nei_of[pre_node]:
            if DP[cur_node] != -1:
                # already visit
                continue
            cnt += dfs(cur_node)
        DP[pre_node] = cnt
        return cnt

    st_node = 0
    dfs(st_node)

    ans = 0
    for cnt in DP:
        if 1 <= cnt <= k-1:
            ans += 1

    return ans


main()
