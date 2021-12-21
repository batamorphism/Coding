import sys
sys.setrecursionlimit(10**9)


def main():
    n_end = int(input())
    nei_of = [[] for _ in range(n_end)]
    for _ in range(n_end-1):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        nei_of[a].append(b)
        nei_of[b].append(a)
    for edge in nei_of:
        edge.sort()

    # dfs
    color = ['w']*n_end
    ans = []

    def dfs(pre_node: int):
        for cur_node in nei_of[pre_node]:
            if color[cur_node] != 'w':
                continue
            color[cur_node] = 'g'
            ans.append(cur_node+1)
            dfs(cur_node)
            ans.append(pre_node+1)
        color[pre_node] = 'b'

    ans.append(0+1)
    color[0] = 'g'
    dfs(0)
    print(*ans)


main()
