import sys
sys.setrecursionlimit(10**9)


def main():
    n, q = map(int, input().split())
    edge_list = []
    for _ in range(n-1):
        a, b = map(int, input().split())
        edge_list.append((a-1, b-1))
    query = [0]*n
    for _ in range(q):
        p, x = map(int, input().split())
        p -= 1
        query[p] += x

    nei_of = [[] for _ in range(n)]
    for edge in edge_list:
        a, b = edge
        nei_of[a].append(b)
        nei_of[b].append(a)

    counter = [0]*n
    color = ['w']*n
    st_node = 0

    def dfs(pre_node, cnt):
        cnt += query[pre_node]
        counter[pre_node] = cnt
        color[pre_node] = 'g'
        for cur_node in nei_of[pre_node]:
            if color[cur_node] != 'w':
                continue
            dfs(cur_node, cnt)

    dfs(st_node, 0)
    print(*counter)


main()
